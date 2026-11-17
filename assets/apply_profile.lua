local mode = "$mode"
local platform = $platform
local usage = $usage

local copy_signature =
    "copyGraphicsSettingPreset(app.cAppGraphicsSetting,ace.cGraphicsSetting.PLATFORM,app.GraphicsSettingUsage.TYPE_Fixed)"
local apply_signature = "setGraphicsSettingInGame(ace.cGraphicsSetting)"

local pc_fields = {
$pc_fields,
}

local render_fields = {
    "_MeshQuality",
    "_MeshletSmallObjectCulling",
    "_ShadowQuality",
    "_ShadowCastDistanceType",
    "_GIQuality",
    "_GroundQuality",
    "_PostSharpness",
}

local profile
local startup_pending = true
local menu_preset_pending = false
local pending = false
local status = "Waiting for the game to load its graphics options."

local function apply_profile()
    local manager = sdk.get_managed_singleton("app.GraphicsManager")
    if not manager then
        return "GraphicsManager is not ready.", true
    end
    local controller = manager:get_field("_AppGraphicsSettingController")
    if not controller then
        return "Graphics controller is not ready.", true
    end
    if manager:get_field("_IsEditGraphicsSettingSaveWork")
        or controller:get_field("_IsWindowModeChangeEventWithStatus")
        or controller:get_field("_IsDisplaySettingChanged")
        or controller:get_field("_IsHDRModeChanged") then
        return "Waiting for the game to finish changing its display settings.", true
    end

    local live = controller:call("get_GraphicsSetting")
    if not live then
        return "Live graphics settings are not ready.", true
    end
    if not profile then
        local instance = sdk.create_instance_global("app.cAppGraphicsSetting")
        if not instance then
            return "Could not allocate app.cAppGraphicsSetting."
        end
        instance:call(".ctor()")
        profile = instance
    end

    if not manager:call(copy_signature, profile, platform, usage) then
        return "The selected NSW2 Default preset was not found in the game's GraphicsPreset."
    end
    for _, field in ipairs(pc_fields) do
        local value = live:get_field(field)
        if value == nil then
            return "Could not read the PC graphics field " .. field .. "."
        end
        profile:set_field(field, value)
    end

    local expected = {}
    for _, field in ipairs(render_fields) do
        local value = profile:get_field(field)
        if value == nil then
            return "Could not read the NSW2 graphics field " .. field .. "."
        end
        expected[field] = value
    end
    manager:call(apply_signature, profile)
    live = controller:call("get_GraphicsSetting")
    if not live then
        return "Live graphics settings are unavailable after applying."
    end
    for _, field in ipairs(render_fields) do
        if live:get_field(field) ~= expected[field] then
            return "Live graphics setting did not match " .. field .. ". Apply again in gameplay."
        end
    end
    return mode .. " applied."
end

local option_type = sdk.find_type_definition("app.cGUISystemModuleOption")
local select_preset = option_type and option_type:get_method(
    "applyGraphicsPresetSetting(app.OptionParamDef.PRESET_QUALITY)"
)
local change_preset_type = option_type and option_type:get_method("onGraphicsPresetSettingsTypeChanged()")
local apply_option = option_type and option_type:get_method(
    "applySetting(app.Option.ID,System.Int32,app.cGUISystemModuleOption.EXCLUDE_FLAG)"
)
local drain_requests = option_type and option_type:get_method("updateRequests()")
if select_preset and change_preset_type and apply_option and drain_requests then
    sdk.hook(select_preset, function(args)
        local tier = sdk.to_int64(args[3]) & 0xff
        if tier <= 4 then
            menu_preset_pending = true
        end
    end, function(retval)
        return retval
    end)
    sdk.hook(change_preset_type, function() end, function(retval)
        menu_preset_pending = true
        return retval
    end)
    sdk.hook(apply_option, function(args)
        local option = sdk.to_int64(args[3]) & 0xffffffff
        local tier = sdk.to_int64(args[4]) & 0xffffffff
        if option == 231 and tier <= 4 then -- app.Option.ID.CUTSCENE_PRESETS
            menu_preset_pending = true
        end
    end, function(retval)
        return retval
    end)
    sdk.hook(drain_requests, function() end, function(retval)
        if startup_pending or menu_preset_pending then
            pending = true
            startup_pending = false
            menu_preset_pending = false
        end
        return retval
    end)
else
    status = "Automatic PC preset sync is unavailable. Apply the profile manually."
    log.error("[MHWS NS2 Graphics Preset for PC] Missing PC preset or option request method.")
end

re.on_application_entry("UpdateBehavior", function()
    if not pending then
        return
    end
    pending = false
    local ok, result, retry = pcall(apply_profile)
    if ok then
        status = result
        pending = retry == true
    else
        status = "Apply failed. See re2_framework_log.txt."
        log.error("[MHWS NS2 Graphics Preset for PC] " .. tostring(result))
    end
end)

re.on_draw_ui(function()
    if imgui.tree_node("MHWS NS2 Graphics Preset for PC - " .. mode) then
        if imgui.button("Apply " .. mode .. " profile") then
            pending = true
            status = "Apply queued."
        end
        imgui.text(status)
        imgui.tree_pop()
    end
end)
