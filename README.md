# MHWS NS2 Graphics Preset for PC

MHWS NS2 Graphics Preset for PC 是《怪物猎人 荒野》的画质 MOD，用于在 PC 平台上启用 Nintendo Switch 2（NS2）平台的画面预设。项目基于 Steam `1.42.0.3` 的游戏数据，分别提供主机版 **Dock** 和掌机版 **Handheld**，对应游戏内的 `NSW2` 和 `NSW2_HANDHELD`。

## 静态 LOD 与 Streaming 策略

- 以本包对应的 NSW2 `Default` 条目为模板覆盖全部 12 条 PC 用途记录，保留各行的平台、用途、色彩、升频、帧率和纹理预算字段。
- 同步 PC 菜单从超高到最低的五档选项。可匹配的字段采用原版 PC 对应选项，例如云使用 `SIMPLIFIED`，网格使用 `STANDARD`。五档共用 PC 标准纹理档和 Balanced 升频质量。
- 使用 NSW2 流送保护配置。距离 10 的近圈保护 mip 1／LOD 1，普通游玩的距离 20 和事件播放的距离 30 保护 mip 2／LOD 2。
- 同步通用和 `ST101`、`ST102`、`ST103` 的四条草地 `FAR` 记录。全局密度、近端和远端裁剪分别为 `1.0 / 10.0 / 100.0`。
- 五档共用沙雪水最低档这一组组件配置。`ST101` 至 `ST105` 的两级地形距离同步为 `120.0 / 90.0`，其余没有 NSW2 对应值的组件参数取原版 PC 沙雪水最低档。
- PC 继续根据设备控制输出、帧率、升频后端和纹理预算。NSW2 的原生分辨率切换及动态纹理上限由单独的平台代码处理。[画质预设与运行路径](docs/nsw2-graphics.md)

## 后处理设置

Dock 的原生 `Default` 开启屏幕空间反射和皮肤次表面散射。Handheld 的原生 `Default` 关闭两项，动态阴影级联从 2 级减为 1 级。

两个模式均启用体积雾。Dock 使用 `96 × 54 × 32` 的体积雾网格并启用自定义降噪。Handheld 使用 `54 × 30 × 32` 并关闭该降噪设置。场景雾和 PC 的显存约束会进一步影响实际渲染。[画质参数表](docs/settings-tables.md)

<div align="center">
<a href="https://github.com/dzxrly/PyREUser3">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-dark.svg">
    <img alt="Powered by PyREUser3" src="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-light.svg">
  </picture>
</a>
</div>

## 安装

从 GitHub Releases 选择 `MHWS_NS2_Graphics_Preset_for_PC_Dock_<version>.zip` 或 `MHWS_NS2_Graphics_Preset_for_PC_Handheld_<version>.zip`。本地构建的压缩包位于 `output/`。将解压出的 `natives` 和 `reframework` 目录放入游戏根目录，并在 REFramework 中开启 **Loose File Loader**。切换模式时用另一份覆盖，重启游戏。[GitHub Releases](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases)

游戏载入保存的设置后会自动应用对应模式。切换普通或过场画质预设时，脚本会在菜单提交后重新应用。游戏有时会将超出原生菜单取值范围的配置显示为「自定义」。要手动应用，可在 REFramework 面板展开 **MHWS NS2 Graphics Preset for PC**，点击 **Apply Dock profile** 或 **Apply Handheld profile**。

每份压缩包包含以下文件。

- `natives/STM/System/SystemSetting/GraphicsPreset.user.3`
- `natives/STM/GameDesign/Common/Option/OptionGraphicsData.user.3`
- `natives/STM/GameDesign/Common/Option/OptionGraphicsPresetData.user.3`
- `natives/STM/System/SystemSetting/AppStreamingControllerManagerSetting.user.3`
- `natives/STM/System/SystemSetting/GrassCullingSetting.user.3`
- `reframework/autorun/MHWS_NSW2onPC.lua`
- `modinfo.ini`

## 本地构建

```powershell
conda activate torch
python -m pip install -r requirements.txt
python tools/build_data.py download
python main.py
```

`data/` 中已有匹配版本的两个元数据文件时，可直接运行 `python main.py`。本项目要求 `PyREUser3>=0.8.1`，用 RSZ 模板读取和回封资源，用 IL2CPP 类型转储解析枚举和字段。

默认同时构建两包。用 `--variant dock` 或 `--variant handheld` 可单独构建，用 `--metadata-dir` 可指定其他匹配的元数据目录。

- `output/MHWS_NS2_Graphics_Preset_for_PC_Dock_<version>.zip`
- `output/MHWS_NS2_Graphics_Preset_for_PC_Handheld_<version>.zip`
- `output/output.log`

`version.json` 的 `version` 字段会写入 `modinfo.ini`，并用于 ZIP 文件名。

## 构建数据

`data/rszMHWS.json` 和 `data/il2cpp_dump.json` 保存在本地 `data/` 供 PyREUser3 读取。Git 忽略这两个大文件，分发时将它们作为专用 `build-data` GitHub Release 中的 assets。

- `rszMHWS.json.gz`
- `rszMHWS.json.gz.sha256`
- `il2cpp_dump.json.gz`
- `il2cpp_dump.json.gz.sha256`

维护者从匹配版本的游戏取得新元数据后，使用 GitHub CLI 登录并上传构建数据。

```powershell
gh auth login
python tools/build_data.py upload
```

脚本会创建或更新 `build-data` Release，覆盖同名 assets。本地 clone 后如缺少元数据，运行以下命令下载、校验并解压回 `data/`。

```powershell
python tools/build_data.py download
```

仓库由环境或 Git 远端识别，也可通过 `--repo owner/name` 显式指定。预演、单文件操作与目录选项见[构建数据工具](tools/README.md)。

## GitHub Actions 发布

`.github/workflows/release.yml` 支持推送 `v*` tag 和手动执行 `Run workflow`。工作流会安装依赖，通过 `python tools/build_data.py download` 获取构建数据，再执行 `python main.py`。

手动执行时用 `version.json` 的版本确定 Release tag，必要时补充 `v` 前缀并创建 tag。工作流检查 Dock 和 Handheld 两份 ZIP 以及 `output/output.log`，然后将三个文件一起发布到对应的 GitHub Release。已存在的同名 assets 会被覆盖。

## 项目结构

- `main.py` 调用 `utils.build.main()`。
- `utils/build.py` 负责读取源资源、构建两种模式、回封验证及打包。
- `utils/__init__.py` 定义构建资源、模式和保留的 PC 字段。
- `utils/patches.py` 修改五个构建资源，维护 PC 菜单目标值。
- `utils/repack.py` 访问 PyREUser3 的实例表和对象引用。
- `utils/verify.py` 比较编辑后的目标数据与重打包后重新读取的数据。
- `utils/package.py` 生成 `modinfo.ini`、Lua 脚本和 ZIP。
- `utils/enums.py` 读取 `data/Enums_Internal.json` 并解析枚举身份。
- `tools/build_data.py` 管理 GitHub Release 中的大体积构建数据。
- `data/natives/STM/` 按游戏相对路径保存原始 `user.3`。
- `assets/` 保存运行时 Lua 和 `modinfo.ini` 模板。
- `docs/` 保存[原始参数表](docs/settings-tables.md)和[平台资源对照](docs/platform-resources.md)。

## AI Agent 修改索引

模式与 PC 保留字段在 `utils/__init__.py` 中维护。每个资源的目标字段由 `utils/patches.py` 中对应函数处理，`utils.build.main()` 决定打包范围。枚举按平台、用途和档位身份匹配。更新源数据时，应复核枚举含义和资源之间的引用关系。

### `GraphicsPreset.user.3`

源文件为 `data/natives/STM/System/SystemSetting/GraphicsPreset.user.3`。根类型为 `AppGraphicsSettingPreset`，由 `utils.patches.patch_graphics_preset()` 处理。

根据 `(平台, 用途)` 选择 `(NSW2, Default)` 或 `(NSW2_HANDHELD, Default)`，复制渲染字段、普通与实验光追子对象及五条关卡地形距离。保留每个 PC 用途的身份和 `PC_GRAPHICS_FIELDS`，以原始值作为各设备设置的起点。

### `OptionGraphicsData.user.3`

源文件为 `data/natives/STM/GameDesign/Common/Option/OptionGraphicsData.user.3`。根类型为 `OptionGraphicsData`，由 `utils.patches.patch_terrain_option()` 处理。

只定位沙雪水的 `LOWEST` 项，并同步地形分块细节开关及 `ST101` 至 `ST105` 的距离。无关卡匹配时仍使用 `INVALID` 行的原始 `180/128`。

### `OptionGraphicsPresetData.user.3`

源文件为 `data/natives/STM/GameDesign/Common/Option/OptionGraphicsPresetData.user.3`。根类型为 `OptionGraphicsPresetData`，由 `utils.patches.patch_option_presets()` 处理。

同步 `_Settings`、`_UpscaleMode`、`_GroundQuality`、`_SandSnowWaterQuality` 和 `_CullingSettings` 五张表。五档保留各自的 `_Quality` 身份，复用相同选项。小物体剔除使用 `HIGHEST`、阈值 `12.0` 和参考分辨率 `720p`。

### `AppStreamingControllerManagerSetting.user.3`

源文件为 `data/natives/STM/System/SystemSetting/AppStreamingControllerManagerSetting.user.3`。根类型为 `AppStreamingControllerManagerSetting`，由 `utils.patches.patch_app_streaming()` 处理。

交换 `_PlatformData` 中 PC 和 NSW2 两行的平台键，使 PC 读取 NSW2 的正常流送保护、事件流送保护和预加载参数。主机与掌机共用这套保护。

### `GrassCullingSetting.user.3`

源文件为 `data/natives/STM/System/SystemSetting/GrassCullingSetting.user.3`。根类型为 `GrassCullingSetting`，由 `utils.patches.patch_grass_culling()` 处理。

按原始预设的草地档位定位通用记录和关卡记录，只写入 `_GlobalDensity`、`_DensityCullingNear` 和 `_DensityCullingFar`。选择其他档位的记录、草地动画距离、实例容量和高度衰减均取游戏原始数据。

### `MossCullingSetting.user.3` 和 `FoliageManagerSetting.user.3`

这两份源文件用于分析。植被管理器引用草地和苔藓资源，苔藓按关卡读取起始距离、动画距离与缩放。引用与平台分支见[平台资源对照](docs/platform-resources.md)。

### `MHWS_NSW2onPC.lua`

源模板为 `assets/apply_profile.lua`。脚本等待原生选项请求处理结束，再通过游戏画质入口应用对应模式。启动、普通预设和过场预设各有触发路径。显示切换或编辑画质期间会延后应用。

## 修改与验证不变量

- 两种模式分别取原始的 NSW2 `Default` 和 `NSW2_HANDHELD` `Default`。12 条 PC 用途保留各自身份，其他平台和共享根表保留原始值。
- 过场及普通菜单的五档共用同一套菜单载荷。每张表的五个 `_Quality` 仍各自唯一。
- 草地按 `FAR` 匹配一条通用记录和三条关卡记录。沙雪水按关卡身份匹配五条地形距离。
- 默认生成两个 ZIP。每包包含五个回封后重新读验的 `user.3`、一个 Lua 脚本和一个 `modinfo.ini`。构建日志位于 `output/output.log`。
- 修改构建或目标参数后运行 `python main.py`，检查两个包、资源回读及构建日志。Lua 的启动和菜单提交时序已有模拟检查，实际游戏内的画面与帧率仍需实测。
