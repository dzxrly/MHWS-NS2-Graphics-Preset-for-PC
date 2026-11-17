# NS2 画质预设与 PC 应用路径

分析基准是本机 Steam `MonsterHunterWilds.exe` 与 `MonsterHunterWilds_dump.exe` 的文件版本 `1.42.0.3`。两者及 REFramework 导出的 `il2cpp_dump.json`、`Enums_Internal.hpp` 和 `rszMHWS.json` 对应 2026 年 10 月 27 日快照，文中 RVA 相对于 Steam 转储的基址 `0x140000000`。数值来自 `mhws_json_to_xlsx/MHWS-in-json/natives/STM` 中按游戏路径排列的导出，关键 `.user.3` 从本机 Steam PAK 重新取出并与 Better4KHDTexture 的原始文件逐字节核对。PAK 提取来源见[平台资源](platform-resources.md)，逐字段数值见[完整参数表](settings-tables.md)。

## 预设的选择

`GraphicsPreset.user.3` 的 `_DataList` 以 `(ace.cGraphicsSetting.PLATFORM, app.GraphicsSettingUsage.TYPE_Fixed)` 为身份。Windows、底座、掌机依次对应平台 5、14、15。引擎在 `ace.user_data.GraphicsSettingPreset<app.cAppGraphicsSetting>.getGraphicsSetting`（RVA `0x6e66790`）按这两个键扫描并返回首条命中。此方法找不到匹配条目时返回空，调用方负责决定是否回退。

| 数据变体 | 用途（Usage） | 引擎选用条件或数据含义 |
| --- | --- | --- |
| Dock | `Default`、`CharMake`、`CutScene` | 常规游玩、捏脸、过场 |
| Dock | `Default_Fast`、`CharMake_Fast`、`CutScene_Fast` | 同三类场景的性能预设 |
| Dock | `FastLoadMode`、`DialoguePlaying` | 快速加载和对话状态独立条目 |
| Handheld | `Default`、`CharMake`、`CutScene`、`DialoguePlaying` | 掌机的常规游玩、捏脸、过场与对话 |

`ace.cGraphicsSetting.getRuntimePlatform`（RVA `0x62216d0`）在目标机器低四位为 11 时，按 `via.SystemService.PerformanceMode` 是否为 `Boost (2)` 选择 Dock 或 Handheld。Windows 低四位为 1，走 PC 或 Steam Deck 平台。性能档选择还涉及 `app.GraphicsManager._IsPerformanceMode`。`getGraphicsSettingUsageDefault`（RVA `0x608d3a0`）的 Dock 性能分支同时要求此标志和 `Boost`，命中后选 `Default_Fast`；Handheld 性能分支选 `Default`。独立的 `via.SystemService.OperationMode`（掌机 0、主机 1）则参与同步间隔判断。

### 两个常规游玩条目

| 字段或效果 | Dock | Handheld |
| --- | --- | --- |
| `_DynamicResolutionMode` | 12，`TARGET_30_LOW_D` | 10，`TARGET_30_LOW` |
| DRS 恢复／降档阈值 | 31.0／33.4 毫秒 | 32.0／33.4 毫秒 |
| `_FilterImageQuality`／`_PostSharpness` | 0.75／0.5 | 0.85／1.0 |
| SSR／解算项 | 开／1 | 关／0 |
| 皮肤屏幕空间次表面散射（SSSSS） | 开 | 关 |
| 阴影投射距离 | `NEAREST` | `NEAREST_H` |
| 体积雾 | 启用自定义降噪，网格档位 2 | 关闭自定义降噪，网格档位 4 |

两者都带有 DLSS Balanced 和两阶段 DLSS 标志。在共同的画质上，两者实际网格质量为 2，主云光线步进分辨率为八分之一，环境光探针用的步进分辨率为三分之一且比例为 0.25。两者的小物体剔除阈值为 12，参考分辨率为 720p。它们使用 `HIGHEST` 网格剔除档，PC 菜单 Lowest 则为 `LOW` 和阈值 8。按剔除档名或枚举整数单独排序会漏掉阈值、分辨率和其它控制量。

可优先比较湿润地面等使用屏幕空间反射的表面、人物皮肤在侧光或逆光下的明暗过渡，以及有明显雾层的远景。底座保留 SSR 和 SSSSS，掌机关掉这两项。阴影查表中 `NEAREST` 与 `NEAREST_H` 的动态级联分别为 2 和 1，代表掌机减少一级动态阴影分段。具体反射、皮肤和雾层差异会受所用材质、场景和 PC 渲染前处理影响。

Dock 的 `Default_Fast` 使用 DRS 11（`TARGET_40_LOW`），阴影质量从 3 降到 2，关闭 SSR、运动模糊和 SSSSS，体积雾改用网格档位 4。捏脸、过场、对话和快速加载还有各自覆盖值。特别是 `FastLoadMode` 与 `Default_Fast` 有不同的 Usage 和载荷。最终两份 MOD 分别选用 Dock 与 Handheld 的 `Default`。

### 输出尺寸与实际帧率

`ace.GraphicsUtil..cctor`（RVA `0x687a970`）初始化三类显示模式索引；从枚举读到的默认标签是 Handheld 810、Dock 1260、Dock 性能档 1080，候选标签还包括 Handheld 720／864 和 Dock 1080／1440。`updateDisplayModeNSW2`（RVA `0x687a740`）经目标机器 11 检查，再按 `Boost` 和游戏的性能标志选择索引，向显示设置调用传递掌机的 `0,8,7` 或底座的 `0,33,38`。这些是内部选择值。对应的实际输出尺寸还取决于后续平台层。

两个 `Default` 的 `_FramerateSetting` 均为 `VARIABLE`、`_MaxFPS` 均为 60；DRS 模式与帧时间阈值描述负载调节目标。NSW2 还有 `updateRequestSyncInterval` 和 `updateSyncInterval`（RVA `0x608a530` 和 `0x608a630`）依据显示、帧率和快载状态请求间隔 1、2 或 4。真实分辨率、锁帧表现和稳定性需要从跑在 NSW2 上的构建取得。同一时期任天堂已发布序章试玩版，Capcom 公布正式版于 2026 年 12 月 4 日发行。[任天堂试玩版公告](https://www.nintendo.com/my/news/article/1T6qe4VgO58mcoN9NAOwow) [Capcom 发行公告](https://www.capcom.co.jp/ir/english/news/html/e260910.html)

## 画质由多张表和运行路径共同决定

- **渲染载荷**。预设记录纹理采样、网格、草木、阴影、体积雾、云、间接光和材质相关配置，也包含光追块。草地距离和密度另有 `GrassCullingSetting` 全局与关卡表，实验光追的关卡值另查 `RayTracingForStageData`。这些独立资源中常见的是质量档或关卡身份，详见[参数表](settings-tables.md)。
- **纹理与模型流式加载**。`GraphicsPreset` 提供纹理档位、纹理预算和网格最小 LOD 的查表载荷。`AppStreamingControllerManager.start`（RVA `0x69c39e0`）另从 `AppStreamingControllerManagerSetting` 找平台保护配置，找不到时回落到 Default。该资源使用独立枚举，PC 是 1，NSW2 是 5，底座和掌机共享一行。普通和事件保护的半径保持相同，10 范围的纹理／模型从 PC 的 mip 2／LOD 2 变为 NSW2 的 mip 1／LOD 1；外圈从 mip 3／LOD 4 变为 mip 2／LOD 2。较低的级别编号意味着优先保护更精细的资源。这项局部差异不能用来推断两平台总显存占用。
- **平台纹理预算**。NSW2 两个 `Default` 的 `_StreamingTextureQuality` 都是 `INVALID (5)`。Windows 在 `doChangeGraphicsSettingBefore`（RVA `0x7bdbffc`）遇到 5 会跳过 PC 纹理档位／预算查表；正常 0–4 档会由 PC 的档位上限约束。NSW2 的 `doSetupNSW2` 则启用分级并将最近纹理和总上限初始化为 2048，`updateTextureStreamingLimitNSW2`（RVA `0x7be2220`）以可用显存减去另一计数器所得的余额控制两项。2048 → 1024 的阈值为低于 500 MiB，回升为高于 600 MiB；1024 → 512 为低于 375 MiB，回升为高于 425 MiB。循环经 `doUpdateAfter` 的机器 11 分支运行。MOD 保留 PC 的纹理预算档位，并另外应用 NSW2 的距离保护。
- **PC 菜单**。`cGUISystemModuleOption.applyGraphicsPresetSetting`（RVA `0x5d1e230`）读取 `OptionGraphicsPresetData`，逐项调用菜单设置器。菜单表决定 PC 最低档的云、阴影、草木和剔除选项，许多选项与 NSW2 原值存在差异。PC 最初选定的 `_UsePresetUsage` 来自 `getInitGraphicsSetting`（RVA `0x608aba0`）的硬件分档与设置初始化路径。只给 `GraphicsPreset` 的条目改标签，无法让 PC 菜单应用完整 NSW2 条目。
- **沙地、雪地和水面**。选项 `SAND_SNOW_WATER_Q.apply`（RVA `0xa2ece60`）从 `OptionGraphicsData` 取出选中的沙雪水条目，将分块细节级别开关及距离数组写入画质对象，还直接调用地形组件的设置器，控制最大细分、着色器切换、纹理覆盖范围等参数。NSW2 两个 Default 的分块细节级别开关均为真，`ST101` 至 `ST105` 的两级距离都是 `120/90`。MOD 将五档菜单指向同一份沙雪水条目，并同步这些已确认值。其余组件参数沿用原版 PC 沙雪水最低档，其中无关卡匹配时使用的 `INVALID` 行仍为 `180/128`。
- **PC 特殊场景**。捏脸、名片、过场载入、对话的 NSW2 专用应用入口存在机器检查，Windows 不进入这些分支。PC 过场走独立的 `changeGraphicsSettingCutScenePC`（RVA `0x608c930`）。因此把 NSW2 的过场行写成另一个 PC Usage 也无法覆盖对应的调用流程。
- **平台专用消费逻辑**。`applyGraphicsSettingCore`（RVA `0x929e390`）在 RVA `0x929f098` 检查目标机器值 11，然后才应用两阶段 DLSS 和对应的滤波／后锐化等字段。Windows 可以在对象里保存 NSW2 数值，这段底座／掌机专用渲染逻辑仍由平台检查控制。NPC 距离、布料、毛发等平台项见[平台资源](platform-resources.md)。
- **Windows 渲染前处理**。`doChangeGraphicsSettingBefore` 还会从 PC 控制器自己的 `_VFogTextureSizeLimit` 重写体积雾纹理大小（RVA `0x7bdbe98`），激活升频且未禁止触发时将可变速率着色（VRS）设为 0（RVA `0x7bdbfe2`）。

## 两份 MOD 的实现与验证边界

构建时按用途键覆盖 `GraphicsPreset` 的 12 条 PC 行，均使用该包的原始 NSW2 Default。平台与用途键，以及 PC 色彩、升频、帧率和纹理预算字段沿用各行原值。光追子对象和分关卡地形距离随模式复制。五档菜单保留各自的 `_Quality` 身份并采用同一组选项。`OptionGraphicsData` 保留各条目的 `_Option`，实际载荷改为对应模式的数据。PC 纹理菜单继续使用原版预算档位，五档起点取标准档。升频质量统一为 Balanced。`GrassCullingSetting` 同步四条 FAR 记录的密度裁剪，`AppStreamingControllerManagerSetting` 交换 PC 与 NSW2 的保护配置键。

PC 的阴影距离应用函数（RVA `0x758be50`）按菜单索引读取 `_Value`，可直接写入 Dock 的 `NEAREST` 或 Handheld 的 `NEAREST_H`。体积雾应用函数（RVA `0x40ef3a0`）直接写入目标体积纹理尺寸、阴影混合和材质降噪三项。网格菜单（RVA `0x6340860`）把同一个 `_Value` 写入网格和 meshlet 的最低 LOD，两种模式都设为 `0`。这些字段随后仍经过 PC 的场景与渲染限制，例如体积雾的独立尺寸上限。

普通和过场预设由 `applyGraphicsPresetSetting` 与 `onGraphicsPresetSettingsTypeChanged`（RVA `0x5d1fae0`）排队，经 `updateRequests`（RVA `0x5d1eb00`）提交。直接布尔项如屏幕空间反射、皮肤次表面散射和景深由预设表选择开关。对多个条目共享同一实际载荷的选项，部分菜单回读会选择首个匹配标签。

启动时 `initializeGraphicsSettingPC`（RVA `0x608a6e0`）会读取 Windows 本地设置。`doReadConfig`（RVA `0x7bdc450`）能直接恢复已保存的雾、反射、运动模糊和阴影值。普通预设只提交发生变化的菜单项。检查预设初始化效果时，应以备份并重建的 PC 配置为起点，并分别验证从已有配置升级时的行为。

要与 NSW2 试玩版或正式版核对，仍需对应版本的画质预设、显示控制和流送资源，以及主机、掌机在同一场景同一镜头下的帧捕获。确定输出同步和平台资源分支需要该版本的类型信息或匹配的反汇编数据。
