# NS2 平台资源与场景设置

## Steam 数据来源

`MonsterHunterWilds.exe` 与 `MonsterHunterWilds_dump.exe` 的文件版本均为 `1.42.0.3`。对当前安装的基础包、子包和补丁包按补丁编号从高到低查找，以下表格记录首次提取到这些资源的包。资源路径均相对于 `natives/STM/`。

| Steam PAK | 资源 |
| --- | --- |
| `re_chunk_000.pak.patch_015.pak` | `System/SystemSetting/GraphicsPreset.user.3`、`System/SystemSetting/AppStreamingControllerManagerSetting.user.3`、`GameDesign/Common/Option/OptionGraphicsData.user.3`、`GameDesign/GUI/Common/_UserData/GraphicsOptionLoadLevel.user.3` |
| `re_chunk_000.pak.patch_014.pak` | `System/SystemSetting/DialogueManagerSetting.user.3` |
| `re_chunk_000.pak.patch_013.pak` | `GameDesign/Common/Option/OptionGraphicsPresetData.user.3`、`GameDesign/GUI/Common/_UserData/GraphicsSettingUsedVramSize.user.3`、`GameDesign/NPC/CommonData/Culling/NpcProcessCullingData.user.3`、`System/SystemSetting/GrassCullingSetting.user.3`、`System/SystemSetting/FoliageManagerSetting.user.3`、`System/SystemSetting/RayTracingForStageData.user.3` |
| `re_chunk_000.pak.patch_012.pak` | `GameDesign/NPC/CommonData/Culling/NpcProcessCullingData_NSW2.user.3`、`GameDesign/Camera/PostEffect/PostEffectCommonSceneBank.user.3`、`System/SystemSetting/GraphicsManagerSetting.user.3`、`System/SystemSetting/MeshManagerSetting.user.3`、`System/SystemSetting/MossCullingSetting.user.3`、`System/SystemSetting/PostEffectManagerBaseSetting.user.3`、`System/SystemSetting/SpeedTreeManagerSetting.user.3` |

参考项目 Better4KHDTexture 的八个构建输入与上述 Steam 提取结果逐字节一致。两份新增的 `FoliageManagerSetting.user.3` 和 `MossCullingSetting.user.3` 在 Downloads、参考项目和 Steam 提取结果中也逐字节一致。Better4KHDTexture 的 `utils/build.py` 未将这两份文件列入八个构建任务。当前 `MHWs_STM_Release.list` 的 328,973 条 `natives/STM/` 路径中没有匹配 `NSW2`、`Switch2`、`/NSW/` 或 `/NX2/` 的记录。旧的 `RETool/MHWs.list` 提供了 `NpcProcessCullingData_NSW2.user.3` 的完整路径，实际从 `patch_012` 解出了文件。路径索引只能覆盖已经命名的条目。

复核时，可在游戏目录以外创建工作目录，把目标资源的完整 `natives/STM/...` 路径逐行写入 `targets.list`，并从最新补丁向基础包执行以下命令。`-skipUnknowns` 将提取范围限制在短名单内，`-dontOverwrite` 保留先提取到的版本。检查命令返回的 `Wrote` 记录与输出文件。

```powershell
& $retool -h $targetList -x -skipUnknowns -noManifest -noExtractDir -dontOverwrite $pak
```

## 与 Better4KHDTexture 的共用资源对照

### 草地、苔藓和植被管理

`FoliageManagerSetting._GrassCullingSetting` 和 `._MossCullingSetting` 直接引用 `System/SystemSetting/` 下的草地、苔藓资源，两个引用的路径均无平台后缀。管理器启用自定义顶点着色器动态阴影及纹理流送距离阈值，阈值为 `200`，关闭植被细节层级的 GPU 模式。该模式的容量字段为 `500`。这些字段位于管理器根部。

`GrassCullingSetting` 有四种通用裁剪档，以及 `ST101`、`ST102`、`ST103` 各四条关卡覆盖。常规裁剪和两个密度开关 `_EnableDensityCulling`、`_EnableDensityCullingConsoleTarget` 都为真，容量为 `80000`，`_ProcessTargetHeight=3.0`。12 条 NSW2 与 NSW2_HANDHELD 预设均配置 `_GrassCullingMode=FAR`、`_EnableFoliageDensityCulling=true`，以及 `_GlobalDensity=1`、`_DensityCullingNear/Far=10/100`。把 `FAR` 应用到 PC 时，引擎侧对应固定枚举值 `6601`。Steam 的原始草地表包含以下数值。

| `FAR` 适用范围 | `_RangeStart` | `_RangeAnimation` | `_DensityCullingNear` | `_DensityCullingFar` |
| --- | ---: | ---: | ---: | ---: |
| 通用 | 50 | 30 | 30 | 600 |
| `ST101` | 90 | 20 | 0 | 600 |
| `ST102` | 30 | 30 | 30 | 600 |
| `ST103` | 90 | 20 | 30 | 600 |

Steam 转储中的两条密度应用路径在不同平台执行。`ace.cGraphicsSettingController.applyGraphicsSettingCore` 在相对虚拟地址 `0x929ebb8` 检查机器类型 `11`，NSW2 直接以预设的密度开关、全局密度和近远距离写入渲染配置。`app.FoliageManager.doUpateGrassCullingData` 在 `0x594cae0` 对 NSW2 提前返回。PC 在同一函数内按关卡和档位选择草地表记录，再由 `doUpdateDensityCulling`（`0x594ce90`）调用同一组渲染参数写入函数，同时应用表中的距离衰减和高度字段。因此，PC 只复制 `GraphicsPreset` 还会使用 PC 草地表的密度和范围。两份 NSW2 Default 的 `FAR` 密度可以通过 PC 的通用 `FAR` 行及三个关卡 `FAR` 覆盖体现，同样使用 `FAR` 的其他 PC 配置也会读到这些值。

Better4KHDTexture 将 4 个通用项和 12 个关卡项的 `_RangeStart` 和 `_RangeAnimation` 乘 `1.5`，将 `_GlobalDensity`、`_DensityCullingFar` 统一为 `1`、`800`，将根部密度裁剪设为假、实例容量设为 `120000`。这些是该模组针对高画质的调整。当前证据支持以 NSW2 的 `1/10/100` 复现其 Default 草地密度范围。草地动画距离、实例容量、距离衰减和高度缺少对应的 NSW2 覆盖值。

`MossCullingSetting` 启用裁剪，容量为 `8000`。它按关卡覆盖 `(起始距离, 动画距离, 起始缩放)`，通用值和 `ST102` 同为 `(50, 0, 0.9)`，`ST104` 为 `(50, 20, 0.9)`，`ST105` 为 `(45, 0, 0.9)`。`app.CCS_MossCullingBAB.updateConstantCS`（`0x6321170`）从植被管理器取苔藓资源。`app.user_data.MossCullingSetting.getData(app.FieldDef.STAGE)`（`0x9792a40`）按关卡选择记录，未找到时使用 `_Data`，随后将三个数值传入计算着色器的常量缓冲。该选表和上传路径不按平台或画质档分支。相邻的 `MeshManagerSetting` 也是根部共用设置，其中毛发容量 `32`、裁剪范围 `10–60`，环境光遮蔽几何容量 `256`、裁剪距离 `50`。掌机毛发缩放由后述的 `app.MeshSetting` 实例另外记录。

### 后处理、纹理流送与分关卡光线追踪

- `VariousDataManagerSetting._PostCommon` 引用 `PostEffectCommonSceneBank`。它的 `_Effects[17]` 存有三个 `ace.PostEffect.cVolumetricFogControlParam`，启用状态为真、假、真，体积纹理均为 `160 × 90 × 128`，`_FogCullingDistance` 分别为 `50`、`0`、`500`。场景动作通过效果编号和 GUID 引用控制项。Better4KHDTexture 把这三个 `_Enabled` 设为假。NSW2 底座和掌机的 Default 都开启普通雾与体积雾，预设中的体积纹理尺寸枚举分别为 `2`、`4`。此外 `TentCameraSetting._PostSceneBank` 引用包含五个已启用体积雾控制项的 `PostEffectTentSceneBank`，`CameraWorkData_LiveCamera` 的相机动作引用 `PostEffectLiveSceneBank`。这些资源按场景和相机使用，直接移植 Common 文件的改动会关闭一部分共用场景雾。
- `RayTracingForStageData` 的 11 行只带 `_Stage` 和 `_ExperimentalRayTrace`。原版全部使用 `_DiffuseRayLength=0`、`_UseRayTracingAO=false` 和 `_UseSolidAngleCulling=true`。`_SpecularRayLength` 和 `_FrustumFarPlane` 同步变化，`ST101` 为 `300`，`ST102` 为 `180`，`ST405` 为 `150`，`ST502` 为 `100`，其余七关为 `60`。Better4KHDTexture 把漫反射距离、镜面距离和远平面统一为 `150/300/300`，开启光追环境光遮蔽并关闭立体角裁剪。NSW2 两份 Default 的 `_RayTracing._Enable=false`，关卡表只携带实验光追数据，普通光追的启用、质量及所用 LOD 位于 `GraphicsPreset` 的预设行。
- Better4KHDTexture 将 `GraphicsManagerSetting._StreamingExpirationFrameCount` 从 `60` 改为 `300`，对话时长另由文件中的 `_Dialogue_StreamingExpirationFrameCount=6000` 控制。两个字段位于共用管理器资源。其 `GraphicsPreset` 还修改根部网格渲染器、`_MPMR` 参数和光追迭代表。例如原版过渡时间 `1.0`、阴影 LOD 和缓存阴影 LOD 为真，参考模组改为 `0.5`、假、假。根部字段可被不同预设共用。带 `_Platform`、`_Usage` 键的 `_DataList` 才包含 NSW2 预设行，根部的画质、显存上限、网格和阴影等表再根据相应设置查值。

草地密度存在可定位的 NSW2 专用代码路径，PC 原版通过草地表应用同一组渲染参数。苔藓、场景体积雾和关卡实验光追尚无证据指向额外的 NSW2 表值。PC 菜单的独立地形路径及其数据修正见[沙地、雪地和水面](nsw2-graphics.md#画质由多张表和运行路径共同决定)。

## NPC 裁剪、生成和布料

`System/SystemSetting/NpcManagerSetting.user.3` 的 `_ProcessCullingData` 指向 `@GameDesign/NPC/CommonData/Culling/NpcProcessCullingData.user`。PC 转储中 `app.mcNpcProcessCullingUpdater.onCreate` 在相对虚拟地址 `0x84878b0` 读取游戏已加载的 `_ProcessCullingData`。这里看到的是加载后的对象，路径前缀在 NSW2 上的解析结果仍需运行记录确认。两个 NPC 裁剪资源的根类型均为 `app.user_data.NpcProcessCullingData`。按 `app.NpcDef.PROCESS_CULLING_LEVEL_Fixed` 和 `app.NpcDef.PROCESS_CULLING_CATEGORY_Fixed` 对齐，通用资源有 8 级、120 条，带 `_NSW2` 后缀的资源有 7 级、105 条。通用资源多出 `VILLAGE_Lowest` 的 15 条。

105 条匹配的记录中有 67 条发生变化，分别涉及 51 个 `_Always` 从 `false` 到 `true` 和 16 个 `_Dist` 缩短。匹配记录的 `_BackDist`、`_Front` 和 `_Enable` 数值一致，三个 `_SkipParams` 也一致。PC 转储的 `updateMain` 在 `0x8487e05` 检查 `_Enable`，随后在 `0x8487e0c` 检查 `_Always`。已启用的类别在 `_Always=true` 时直接裁剪，在 `_Always=false` 时进入 `isCulling`（`0x50160f0`）并根据距离与方向判断。

| 字段所属裁剪类别 | 裁剪等级 | `_Dist` 通用值 → NSW2 值 |
| --- | --- | --- |
| `OFF_DRAW_GAMEOBJECT` | `VILLAGE_SuperHigh` / `High` / `Middle` / `Low` / `HUNTER` | 150 → 75 / 100 → 50 / 80 → 40 / 65 → 35 / 100 → 50 |
| `ACTION_EMULATION_MODE` | `VILLAGE_SuperHigh` / `High` / `Middle` / `Low` / `HUNTER` | 100 → 50 / 100 → 40 / 100 → 30 / 100 → 30 / 100 → 50 |
| `OFF_UPDATE_LOOK_AT` | `VILLAGE_SuperHigh` / `High` | 50 → 25 / 30 → 15 |
| `SKIP_UPDATE` / `SKIP_UPDATE_LV2` | `VILLAGE_Low` | 30 → 10 / 40 → 20 |
| `OFF_UPDATE_FOOTEFFECT_GROUNDDETECT` | `HUNTER` / `PARTNER` | 80 → 20 / 80 → 20 |

数据库中的 `GameDesign/NPC/Data/FieldUnit/_Package/NpcFieldUnitPackage_ut102_01.user.3` 至 `ut102_03.user.3` 把 `STRUCT__InstantiateRange_NSW2__Value` 设为 `50`，通用 `_InstantiateRange` 为 `100`。另外十份带该可选字段的包未启用它。这项设置影响 NPC 生成范围，与上表已经生成的 NPC 的绘制和更新距离分属不同环节。

导出中出现 115 个带 `app.ClothSetting._IsDestroyComponent_NSW2` 的实例，其中 10 个为 `true`。对应 `GameDesign/NPC/_Prefab/Model/Human/` 中的 `ch04_205_0000`、`ch04_204_0000`、`ch04_201_0002`、`ch04_201_0000`、`ch04_200_0001`、`ch04_200_0000`，以及 `GameDesign/Accessory/_Prefab/NPC/Attach_Mantle/` 中的 `Acc111_252`、`Acc111_210`、`Acc111_209`、`Acc111_206`。这些标记的作用对象是布料组件。

`DialogueManagerSetting` 为事件对话开始前的流送等待分别配置了通用上限 `2` 秒和 `_LimitWaitStreamingSecWhenEventDialogueStart_NSW2` 上限 `4` 秒。这是对话流送时序参数。

## 毛发、环境光遮蔽和表情细节

`app.MeshSetting._ShellFurBaseScaleHandheld` 在提供的 5,215 个预制体导出中出现 7,655 次，值均为 `0.25`。读取当前 Steam 版 `GameFlow/Title/TitleField/st101/Layout.scn.21` 也得到三个值为 `0.25` 的实例。实际尺寸和视觉效果取决于运行时选用该字段的网格与材质。

类型定义中，`app.ShadowUtil.AO_SETTING`、`app.ShadowDistanceController` 和 `app.EventShadowController` 有 `STRUCT__AOEfficiencyNSW2__IsOverwrite` 与 `STRUCT__AOEfficiencyNSW2__Value`，可表示 NSW2 的环境光遮蔽强度覆盖。`ace.cMotionLodControl` 有 `STRUCT_Options_DisableOffsetExpressionLodOnNSW2`，指向表情细节层级处理。提供的数据库未出现这些字段的实例值。用相同版本的 `rszMHWS.json` 读取了 77 个取样场景，覆盖已列出的地图根场景和标题场景，未发现上述覆盖实例。另取样的一份对话预制体因通用网格字段的类型推断冲突无法解码。场景检查使用了本机的 REE-Lib。[REE-Lib 场景读取说明](https://github.com/kagenocookie/RE-Engine-Lib#read-and-modify-a-scn20-file)

## 模组范围与证据缺口

两个包分别将 Dock 或 Handheld 配置映射到 `GraphicsPreset` 的 12 条 PC 记录。`OptionGraphicsPresetData` 同步五个 PC 菜单档位的选项，`OptionGraphicsData` 给五档共用的沙雪水设置提供 NSW2 关卡距离。`AppStreamingControllerManagerSetting` 提供 NSW2 流送保护参数。`GrassCullingSetting` 对齐通用 `FAR` 和三个关卡 `FAR` 行的 `_GlobalDensity`、`_DensityCullingNear`、`_DensityCullingFar`。原有全局密度已经是 `1`，实际变化集中在近远距离。`FoliageManagerSetting` 和 `MossCullingSetting` 的原始文件可用于对照。REFramework 脚本在 PC 菜单排队的修改处理完毕后重新应用所选配置。

NPC 处理、生成、布料、毛发、环境光遮蔽、表情细节、对话时序及平台专用网格或材质属于独立的游戏资源或平台分支。现有通用裁剪路径与旧 NSW2 资源的等级集合存在差异，直接覆盖会让当前资源中的 `VILLAGE_Lowest` 条目消失。

要确定 NSW2 真机上的可见效果，需要同一游戏版本的底座和掌机运行记录。资源加载日志需包含 `@GameDesign/NPC/CommonData/Culling/NpcProcessCullingData.user` 的实际解析路径，以及被测试地图和过场使用的 `.scn`、`.pfb`。解析后的场景数据或运行时组件转储需包含前述三个环境光遮蔽类和 `ace.cMotionLodControl` 的实例字段。若要逐项核对真机贴图、网格、材质和着色器，还需要这些场景在 NSW2 上实际引用的资源清单与对应文件，以及同视角的捕获帧。Steam 路径列表和 PC 可执行文件只能核实 STM 侧的数据与代码。
