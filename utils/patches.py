from __future__ import annotations

from copy import deepcopy

from . import GRAPHICS_PLATFORM, GRAPHICS_USAGE, PC_GRAPHICS_FIELDS, STREAMING_PLATFORM
from .enums import EnumLookup, enum_int
from .repack import (
    JsonDict,
    fields,
    insert_instances_before,
    instance,
    iter_ref_fields,
    ref_id,
    root_instance,
)

PC_TERRAIN_OPTION = "[4] LOWEST"


def graphics_profile(data: JsonDict, platform: int, usage: int) -> JsonDict:
    root = root_instance(data=data, class_suffix="AppGraphicsSettingPreset")
    matches = [
        entry
        for entry in iter_ref_fields(data=data, refs=root["fields"]["_DataList"])
        if enum_int(value=entry["_Platform"]) == platform
        and enum_int(value=entry["_Usage"]) == usage
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected one GraphicsPreset row for ({platform}, {usage}), found {len(matches)}"
        )
    return matches[0]


def patch_graphics_preset(
    data: JsonDict, profile: JsonDict, enums: EnumLookup
) -> list[int]:
    root = root_instance(data=data, class_suffix="AppGraphicsSettingPreset")
    refs = root["fields"]["_DataList"]
    rows = list(iter_ref_fields(data=data, refs=refs))
    pc = enums.value(enum_type=GRAPHICS_PLATFORM, member="PC")
    targets = [row for row in rows if enum_int(value=row["_Platform"]) == pc]
    usages = [enum_int(value=row["_Usage"]) for row in targets]
    menu_usages = {
        enums.value(enum_type=GRAPHICS_USAGE, member=member)
        for member in ("PC_Lowest", "PC_Low", "PC_Middle", "PC_High", "PC_Highest")
    }
    if (
        None in usages
        or len(usages) != len(set(usages))
        or not menu_usages.issubset(usages)
    ):
        raise ValueError(f"incomplete or duplicate PC GraphicsPreset usages: {usages}")

    nested_fields = ("_RayTracing", "_ExperimentalRayTrace")
    stage_lods = "_GroundSwitchLodDistanceArray"
    stages = [instance(data=data, ref=ref) for ref in profile[stage_lods]]
    if any(row[stage_lods] for row in targets):
        raise ValueError("expected empty PC stage GroundLOD tables before the patch")
    payload = {
        name: value
        for name, value in profile.items()
        if name not in PC_GRAPHICS_FIELDS
        and name not in nested_fields
        and name != stage_lods
    }
    for name in nested_fields:
        ref_ids = [row[name]["ref_instance_id"] for row in rows]
        target_ids = [row[name]["ref_instance_id"] for row in targets]
        if any(ref_ids.count(ref_id) != 1 for ref_id in target_ids):
            raise ValueError(f"{name} contains a shared PC instance")
    for row in targets:
        if row.keys() != profile.keys():
            raise ValueError(
                f"PC usage {row['_Usage']} has a different graphics layout"
            )
        for name in nested_fields:
            source = instance(data=data, ref=profile[name])
            target = instance(data=data, ref=row[name])
            if (
                source["_class"] != target["_class"]
                or source["fields"].keys() != target["fields"].keys()
            ):
                raise ValueError(
                    f"PC usage {row['_Usage']} has a different {name} layout"
                )
            target["fields"] = deepcopy(source["fields"])
        row.update(deepcopy(payload))
    if stages:
        before = min(
            ref_id(ref=ref)
            for ref, row in zip(refs, rows)
            if enum_int(value=row["_Platform"]) == pc
        )
        added = [deepcopy(stage) for _ in targets for stage in stages]
        insert_instances_before(data=data, before=before, added=added)
        for index, row in enumerate(targets):
            start = before + index * len(stages)
            row[stage_lods] = [
                {"ref_instance_id": instance_id}
                for instance_id in range(start, start + len(stages))
            ]
    return [usage for usage in usages if usage is not None]


def patch_option_presets(
    data: JsonDict,
    profile: JsonDict,
    menu_options: dict[str, str],
) -> None:
    root = root_instance(data=data, class_suffix="OptionGraphicsPresetData")["fields"]
    lowest = next(
        row
        for row in iter_ref_fields(data=data, refs=root["_Settings"])
        if enum_int(value=row["_Quality"]) == 4
    )
    settings = {
        **{
            name: fields(data=data, ref=ref)["_Value"]
            for name, ref in lowest.items()
            if name != "_Quality"
        },
        **{name: choice for name, choice in menu_options.items() if name in lowest},
        # PC needs an explicit tier. STANDARD uses the middle 1024 texture cap.
        "_TextureQuality": "[2] STANDARD",
        "_ScreenSpaceReflection": "[0] ON" if profile["_SSR_Enable"] else "[1] OFF",
        "_SsssScattering": "[0] ON" if profile["_SSSSS_Enable"] else "[1] OFF",
        "_DepthOfField": "[0] ON" if profile["_DOF_Enable"] else "[1] OFF",
    }

    for table in (
        "_Settings",
        "_UpscaleMode",
        "_GroundQuality",
        "_SandSnowWaterQuality",
        "_CullingSettings",
    ):
        rows = list(iter_ref_fields(data=data, refs=root[table]))
        qualities = [enum_int(value=row["_Quality"]) for row in rows]
        if len(rows) != 5 or set(qualities) != set(range(5)):
            raise ValueError(
                f"{table} does not contain all five PC qualities: {qualities}"
            )
        for row in rows:
            if table == "_Settings":
                for name, value in settings.items():
                    fields(data=data, ref=row[name])["_Value"] = value
            elif table == "_GroundQuality":
                row["_Value"] = menu_options["_GroundQuality"]
            elif table == "_UpscaleMode":
                # PC's menu enum has a different value for Balanced from the engine enum.
                row["_Value"] = "[2] BALANCED"
            elif table == "_SandSnowWaterQuality":
                row["_Value"] = menu_options["_SandSnowWaterQuality"]
            else:
                resolution = profile["_SmallObjectCullingResolution"]
                row["_Value"] = profile["_MeshCullingSetting"]
                row["_SmallObjectCulling"] = profile["_MeshletSmallObjectCulling"]
                row["_MPMRSmallObjectCullingResolution"] = (
                    f"[{resolution}] MPMRSmallObjectCullingResolution_{resolution}p"
                )


def patch_option_graphics(
    data: JsonDict,
    graphics: JsonDict,
    profile: JsonDict,
    enums: EnumLookup,
) -> dict[str, str]:
    root = root_instance(data=data, class_suffix="OptionGraphicsData")["fields"]
    render_quality = "via.render.RenderConfig.Quality"
    ray_tracing = fields(data=graphics, ref=profile["_RayTracing"])
    experimental_rt = fields(data=graphics, ref=profile["_ExperimentalRayTrace"])
    mesh_lod = profile["_StreamingMeshMinimumLOD"]
    if mesh_lod != profile["_StreamingMeshletMinimumLOD"]:
        raise ValueError("the PC mesh option takes one value for mesh and meshlet LOD")
    targets = {
        "_AntiAliasing": {
            "_Value": enums.label(
                enum_type="via.render.RenderConfig.AntiAliasingType",
                value=profile["_AntiAliasing"],
            ),
        },
        "_RayTracing": {
            "_Enable": ray_tracing["_Enable"],
            "_Quality": enums.label(
                enum_type=render_quality, value=ray_tracing["_Quality"]
            ),
            "_RayTracingResRatio": experimental_rt["_RayTracingResRatio"],
        },
        "_TextureFiltering": {
            "_Value": enums.label(
                enum_type="via.render.SamplerQuality",
                value=profile["_SamplerQuality"],
            ),
        },
        "_MeshQuality": {"_Value": mesh_lod},
        "_SkyCloudQuality": {
            name: profile[name]
            for name in (
                "_MainRaymarchResolution",
                "_IBLRaymarchResolution",
                "_IBLRaymarchScale",
                "_IBLPartialDrawFrame",
                "_MainRaymarchNum",
                "_ShadowRaymarchNum",
                "_ResourceOption",
                "_UpscaleBoundaryBlendAdjuster",
            )
        },
        "_PlantQuality": {"_Value": profile["_StreamingMeshMinimumLODSpeedTree"]},
        "_PlantShaking": {
            "_Leaf": profile["_SpeedTreeWind_Leaf"],
            "_Branch": profile["_SpeedTreeWind_Branch"],
            "_Global": profile["_SpeedTreeWind_Global"],
        },
        "_PlantDensity": {"_Value": profile["_GrassCullingMode"]},
        "_PlantCollision": {"_Value": int(not profile["_GrassPushCollision"])},
        "_ShadowQuality": {
            "_Value": enums.label(
                enum_type=render_quality, value=profile["_ShadowQuality"]
            ),
        },
        "_ContactShadow": {
            "_Value": enums.label(
                enum_type="via.render.RenderConfig.OptionSetting",
                value=profile["_ContactShadowSetting"],
            ),
        },
        "_AmbientOcclusion": {
            "_AOSetting": enums.label(
                enum_type=render_quality, value=profile["_AOSetting"]
            ),
            "_SSAO_HalfResolution": profile["_SSAO_HalfResolution"],
        },
        "_Bloom": {
            "_Enable": profile["_Bloom_Enable"],
            "_ReductionLevel": profile["_Bloom_ReductionLevel"],
        },
        "_VolumeFogQuality": {
            "_Value": enums.label(
                enum_type="via.render.VolumetricFogControl.TextureSize",
                value=profile["_VolumetricFogControl_TextureSize"],
            ),
            "_ShadowCullingBlendFactorScale": profile[
                "_VolumetricFogControl_ShadowCullingBlendFactorScale"
            ],
            "_CustomMaterialImproveNoise": profile[
                "_VolumetricFogControl_CustomMaterialImproveNoise"
            ],
        },
        "_VariableRateShading": {
            "_Value": enums.label(
                enum_type="via.render.RenderConfig.VRSType",
                value=profile["_VRSSetting"],
            ),
        },
        "_FurQuality": {"_Value": profile["_UseLowShellFur"]},
        "_WindFluidSimulation": {"_Value": profile["_WindSimulationQuality"]},
        "_GroundQuality": {"_Value": profile["_GroundQuality"]},
        "_WaterFluidEffect": {"_Value": profile["_UseLowWaterSimulation"]},
        "_DistantShadow": {"_Value": profile["_UseLowResolutionSDF"]},
        "_ShadowCastDistance": {
            "_Value": enums.label(
                enum_type="ace.cGraphicsSetting.SHADOW_CAST_DISTANCE_TYPE",
                value=profile["_ShadowCastDistanceType"],
            ),
        },
        "_AmbientLight": {
            "_Value": enums.label(
                enum_type="ace.cGraphicsSetting.GI_QUALITY",
                value=profile["_GIQuality"],
            ),
        },
    }
    menu_options = {}
    for group, values in targets.items():
        items = list(
            iter_ref_fields(
                data=data, refs=fields(data=data, ref=root[group])["_Items"]
            ),
        )
        for item in items:
            missing_fields = values.keys() - item.keys()
            if missing_fields:
                raise ValueError(
                    f"{group} {item['_Option']} is missing {sorted(missing_fields)}"
                )
            item.update(values)
        # The PC getters return the first matching item when payloads coincide.
        preset_group = "_TextureFilter" if group == "_TextureFiltering" else group
        menu_options[preset_group] = items[0]["_Option"]

    terrain = list(
        iter_ref_fields(
            data=data,
            refs=fields(data=data, ref=root["_SandSnowWaterQuality"])["_Items"],
        ),
    )
    patch_terrain_options(data=data, graphics=graphics, profile=profile, items=terrain)
    menu_options["_SandSnowWaterQuality"] = PC_TERRAIN_OPTION
    return menu_options


def patch_terrain_options(
    data: JsonDict,
    graphics: JsonDict,
    profile: JsonDict,
    items: list[JsonDict],
) -> None:
    stage_array = "_GroundSwitchLodDistanceArray"
    base = next(item for item in items if item["_Option"] == PC_TERRAIN_OPTION)
    targets = {
        name: value
        for name, value in base.items()
        if name not in ("_Option", stage_array)
    }
    targets["_EnableGroundSwtichLodPerPatch"] = profile[
        "_EnableGroundSwtichLodPerPatch"
    ]
    stages = {
        row["_StageID_Fixed"]: (row["_LOD0"], row["_LOD1"])
        for row in iter_ref_fields(data=data, refs=base[stage_array])
    }
    for row in iter_ref_fields(data=graphics, refs=profile[stage_array]):
        stages[row["_StageID_Fixed"]] = row["_LOD0"], row["_LOD1"]
    for item in items:
        item.update(targets)
        rows = {
            row["_StageID_Fixed"]: row
            for row in iter_ref_fields(data=data, refs=item[stage_array])
        }
        if rows.keys() != stages.keys():
            raise ValueError(f"{item['_Option']} has different terrain stages")
        for stage, row in rows.items():
            row["_LOD0"], row["_LOD1"] = stages[stage]


def patch_grass_culling(data: JsonDict, profile: JsonDict, enums: EnumLookup) -> int:
    root = root_instance(data=data, class_suffix="GrassCullingSetting")["fields"]
    mode = profile["_GrassCullingMode"].split(" ", maxsplit=1)[1]
    fixed_mode = enums.value(
        enum_type="app.GrassCulling.CULLING_MODE_Fixed", member=mode
    )
    density = {
        name: profile[name]
        for name in ("_GlobalDensity", "_DensityCullingNear", "_DensityCullingFar")
    }
    selected = [
        row
        for row in iter_ref_fields(
            data=data, refs=[*root["_Data"], *root["_StageData"]]
        )
        if enum_int(value=row["_CullingMode"]) == fixed_mode
    ]
    if not selected:
        raise ValueError(f"GrassCullingSetting has no {mode} rows")
    for row in selected:
        row.update(density)
    return len(selected)


def patch_app_streaming(data: JsonDict, enums: EnumLookup) -> list[str]:
    root = root_instance(data=data, class_suffix="AppStreamingControllerManagerSetting")
    entries = list(iter_ref_fields(data=data, refs=root["fields"]["_PlatformData"]))
    by_platform = {enum_int(value=entry["_Platform"]): entry for entry in entries}
    if len(by_platform) != len(entries):
        raise ValueError(
            "AppStreamingControllerManagerSetting contains duplicate platform keys"
        )
    pc = enums.value(enum_type=STREAMING_PLATFORM, member="PC")
    nsw2 = enums.value(enum_type=STREAMING_PLATFORM, member="NSW2")
    pc_entry = by_platform[pc]
    nsw2_entry = by_platform[nsw2]
    pc_entry["_Platform"], nsw2_entry["_Platform"] = (
        nsw2_entry["_Platform"],
        pc_entry["_Platform"],
    )
    return [
        f"Original PC row _Platform: {pc} -> {nsw2}",
        f"Original NSW2 row _Platform: {nsw2} -> {pc}",
    ]
