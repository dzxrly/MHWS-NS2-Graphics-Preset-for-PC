"""Build inputs and package variants."""

from pathlib import Path

SYSTEM_SETTING = Path("natives/STM/System/SystemSetting")
GRAPHICS_PRESET = SYSTEM_SETTING / "GraphicsPreset.user.3"
APP_STREAMING = SYSTEM_SETTING / "AppStreamingControllerManagerSetting.user.3"
GRASS_CULLING = SYSTEM_SETTING / "GrassCullingSetting.user.3"
OPTION_PRESET = Path(
    "natives/STM/GameDesign/Common/Option/OptionGraphicsPresetData.user.3"
)
OPTION_GRAPHICS = OPTION_PRESET.with_name("OptionGraphicsData.user.3")

GRAPHICS_PLATFORM = "ace.cGraphicsSetting.PLATFORM"
GRAPHICS_USAGE = "app.GraphicsSettingUsage.TYPE_Fixed"
STREAMING_PLATFORM = "app.StreamingControllerPlatform.TYPE"

PC_GRAPHICS_FIELDS = (
    "_Platform",
    "_Usage",
    "_ColorSpace",
    "_OpenColorIOSDRConfig",
    "_UpscaleAlgorithm",
    "_UpscalingQuality",
    "_ImageQualityRate",
    "_DynamicResolutionMode",
    "_FramerateSetting",
    "_MaxFPS",
    "_DLSSPreset",
    "_EnableTwoStepDLSS",
    "_StreamingTextureQuality",
)

VARIANTS = {"dock": "NSW2", "handheld": "NSW2_HANDHELD"}
