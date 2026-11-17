# NS2 画质参数表

数据来自 2026-10-27 本地游戏 JSON 导出。路径以 `C:\Software\mhws\mhws_json_to_xlsx\MHWS-in-json` 为根。枚举按该目录的 `Enums_Internal.json` 解码。Dock、Handheld 和 PC Lowest 分别对应平台 `14`、`15`、`5`，PC Lowest 的用途值为 `99`。对照表中的等号表示与同一行的 Dock 值一致。

## 全部 NSW2 预设

源文件为 `natives/STM/System/SystemSetting/GraphicsPreset.user.3.json`，对象位于 `app.user_data.AppGraphicsSettingPreset._DataList`。行按原数组顺序列出，索引从零开始。使用场景名来自 `app.GraphicsSettingUsage.TYPE_Fixed`。

| 索引 | 平台 | Usage | 动态分辨率 | 上采样 | 质量 | 两步 DLSS | 滤波 | 锐化 | 帧率上限字段 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | `NSW2` | `0 Default` | `[12] TARGET_30_LOW_D` | `[1] DLSS` | `[5] Balanced` | `true` | `0.75` | `0.5` | `60` |
| 44 | `NSW2` | `1 CharMake` | `[0] DISABLE` | `[1] DLSS` | `[5] Balanced` | `true` | `0.75` | `0.5` | `60` |
| 45 | `NSW2` | `2 CutScene` | `[0] DISABLE` | `[1] DLSS` | `[2] UltraQuality` | `true` | `0.755` | `0.25` | `60` |
| 46 | `NSW2` | `242 DialoguePlaying` | `[0] DISABLE` | `[1] DLSS` | `[5] Balanced` | `true` | `0.75` | `0.5` | `60` |
| 47 | `NSW2` | `6 Default_Fast` | `[11] TARGET_40_LOW` | `[1] DLSS` | `[5] Balanced` | `true` | `0.85` | `0.5` | `60` |
| 48 | `NSW2` | `7 CharMake_Fast` | `[0] DISABLE` | `[1] DLSS` | `[5] Balanced` | `true` | `0.85` | `0.5` | `60` |
| 49 | `NSW2` | `8 CutScene_Fast` | `[0] DISABLE` | `[1] DLSS` | `[2] UltraQuality` | `true` | `0.755` | `0.25` | `60` |
| 50 | `NSW2_HANDHELD` | `0 Default` | `[10] TARGET_30_LOW` | `[1] DLSS` | `[5] Balanced` | `true` | `0.85` | `1.0` | `60` |
| 51 | `NSW2_HANDHELD` | `1 CharMake` | `[0] DISABLE` | `[1] DLSS` | `[5] Balanced` | `true` | `0.85` | `1.0` | `60` |
| 52 | `NSW2_HANDHELD` | `2 CutScene` | `[0] DISABLE` | `[1] DLSS` | `[2] UltraQuality` | `true` | `0.755` | `0.25` | `60` |
| 53 | `NSW2_HANDHELD` | `242 DialoguePlaying` | `[10] TARGET_30_LOW` | `[1] DLSS` | `[5] Balanced` | `true` | `0.85` | `1.0` | `60` |
| 54 | `NSW2` | `241 FastLoadMode` | `[0] DISABLE` | `[0] NONE` | `[7] MaxPerformance` | `false` | `0.85` | `1.0` | `60` |

上述十二条的 `_FramerateSetting` 都为 `[2] VARIABLE`，`_DLSSPreset` 都为 `[0] Default`。动态分辨率模式里的 30 或 40 表示配置的目标类别，实际帧率需要运行测量。

## Dock Default、Handheld Default 与 PC Lowest 的完整载荷

仍取自 `GraphicsPreset._DataList`。嵌套对象按字段路径展开。地形各场景的距离以 `_StageID_Fixed` 对齐。仅此表的长字段路径省略导出器添加的类名包装。

### 顶层字段

| 字段 | Dock Default | Handheld Default | PC Lowest |
| --- | --- | --- | --- |
| `_FovHackEnable` | `false` | = | = |
| `_Fov` | `40.0` | = | = |
| `_FramerateSetting` | `[2] VARIABLE` | = | = |
| `_MaxFPS` | `60` | = | `120` |
| `_ImageQualityRate` | `1.0` | = | = |
| `_PresentSkipTimerAfterHomeMenu` | `0.0` | = | = |
| `_RenderingMethod` | `0` | = | = |
| `_DeinterlaceType` | `1` | = | = |
| `_ColorSpace` | `1` | = | = |
| `_OpenColorIOSDRConfig` | `[0] Auto` | = | = |
| `_AntiAliasing` | `[1] TAA` | = | = |
| `_SharpnessSetting` | `4` | = | = |
| `_EffectMaskScaleForPSSRReactiveMask` | `0.25` | = | = |
| `_DownsamplerSetting` | `1` | = | = |
| `_ShadowQuality` | `[3] HIGH` | = | `[2] STANDARD` |
| `_AOSetting` | `[1] LOW` | = | = |
| `_GIPointCloudMinLod` | `1` | = | `0` |
| `_DOFCircular_FarKernelRadius` | `0` | = | `2` |
| `_DOFCircular_NearKernelRadius` | `0` | = | `2` |
| `_SSR_ResolvePoint` | `[1] SSRResolvePointNum_2` | `[0] SSRResolvePointNum_1` | = |
| `_VolumetricFogControl_TextureSize` | `[2] W96xH54xD32` | `[4] W54xH30xD32` | `[3] W96xH54xD64` |
| `_VolumetricFogControl_CustomMaterialImproveNoise` | `true` | `false` | = |
| `_VolumetricFogControl_ShadowCullingBlendFactorScale` | `1.0` | = | `0.0` |
| `_UseSkyIBLAsyncSeparate` | `true` | = | `false` |
| `_ContactShadowSetting` | `[2] CUSTOM` | = | = |
| `_ContactShadowThickness` | `0.05` | = | = |
| `_ShadowCacheEnable` | `true` | = | = |
| `_UseLowResolutionSDF` | `true` | = | = |
| `_GlobalSDFUpdateFrequency` | `[0] UltraLow` | = | = |
| `_PrioritizeGlobalSDFGridByViewFrustum` | `true` | = | = |
| `_GlobalSDFCullingScale` | `4.0` | = | `1.0` |
| `_DelayGlobalSDFScrollUpdate` | `true` | = | `false` |
| `_GlobalSDFMaximumCullingSize` | `16.0` | = | `4.0` |
| `_SDFShadowTarget` | `1` | = | `0` |
| `_TemporalBlendSDFShadow` | `false` | = | = |
| `_ShadowCasterCulling` | `false` | = | `true` |
| `_EnhancedShadowCasterCulling` | `false` | = | `true` |
| `_GlobalSDFMinimumInstanceSize` | `2.5` | = | `1.0` |
| `_ShrinkShadowmapFilterSampleWidthMax` | `128` | = | = |
| `_ForceFullUpdateGlobalSDFOnCut` | `true` | = | = |
| `_LowQualitySDFShadow` | `true` | = | `false` |
| `_DetailSDFShadowRange` | `60.0` | = | = |
| `_TransparentBufferQuality` | `3` | = | `4` |
| `_GIMode` | `[2] DynamicProbe` | = | = |
| `_ProbeTraceAccumulationWeight` | `0.0` | = | `0.975` |
| `_ProbeTraceUpdateDivisionType` | `8` | = | `1` |
| `_ProbeTraceRayAccumulationFrame` | `8` | = | `1` |
| `_GIPointCloudStreamingDistance` | `512.0` | = | = |
| `_SolidGBufferPrepassEarly` | `true` | = | `false` |
| `_AllowOverCommitMesh` | `false` | = | `true` |
| `_StreamingMeshOvercommitLOD` | `0` | = | `2` |
| `_LODResolustion` | `720` | = | `0` |
| `_SmallObjectCullingResolution` | `720` | = | `0` |
| `_MeshletSmallObjectCulling` | `12.0` | = | `0.0` |
| `_MeshletLodBias` | `0` | = | = |
| `_ShadowCastLODBiasMPMR` | `2.0` | = | `0.0` |
| `_ShadowCastSpeedTreeLODBiasMPMR` | `2.0` | = | `0.0` |
| `_InstanceOcclusionTestBias` | `2` | = | `3` |
| `_ClusterOcclusionTestBias` | `2` | = | `3` |
| `_AsyncGeometryTransform` | `false` | = | `true` |
| `_MeshQuality` | `2` | = | = |
| `_SamplerQuality` | `2` | = | `3` |
| `_SecondarySamplerQuality` | `2` | = | `3` |
| `_BakedResourceTextureSizeOffset` | `0` | = | = |
| `_VRSSetting` | `0` | = | `2` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[10] TARGET_30_LOW` | `[0] DISABLE` |
| `_PerPrimitiveVRSEnable` | `true` | = | = |
| `_ShaderLodGlobalValue` | `0` | = | = |
| `_GIPointCloudQuality` | `2` | = | `1` |
| `_StrandShadingQuality` | `2` | = | = |
| `_AutomaticSamplerQuality` | `0` | = | `3` |
| `_SecondaryAutomaticSamplerQuality` | `0` | = | `3` |
| `_RoughTransparentLowResolution` | `false` | = | = |
| `_DynamicShadowEnable` | `true` | = | = |
| `_SSAO_ProjectionScale` | `2000.0` | = | = |
| `_SSAO_HalfResolution` | `true` | = | = |
| `_GeometryAO_IgnoreDynamicObject` | `true` | = | = |
| `_GeometryAO_HalfResolution` | `true` | = | = |
| `_Bloom_Enable` | `true` | = | = |
| `_Bloom_ReductionLevel` | `3` | = | `5` |
| `_Bloom_IsHighPrecision` | `false` | = | = |
| `_Bloom_V3_LWMode` | `true` | = | `false` |
| `_DOF_Enable` | `true` | = | = |
| `_DOFCircular_Enable` | `true` | = | = |
| `_DOFCircular_TwoComponent` | `false` | = | `true` |
| `_SSR_Enable` | `true` | `false` | = |
| `_SSR_RougnessLimit` | `0.2` | = | = |
| `_SSR_DetailRoughnessRatio` | `0.2` | = | = |
| `_SSSSS_Enable` | `true` | `false` | = |
| `_Fog_Enable` | `true` | = | = |
| `_VolumetricFogControl_Enable` | `true` | = | = |
| `_MotionBlur_Enable` | `true` | = | = |
| `_FilmGrain_Enable` | `true` | = | = |
| `_LensFlare_Enable` | `true` | = | = |
| `_GodRay_Enable` | `true` | = | = |
| `_LensDistortionSetting` | `0` | = | = |
| `_LocalExposureBlurredLogDownsampleSize` | `2` | = | `0` |
| `_LodBias` | `0` | = | = |
| `_LodRate` | `1.0` | = | = |
| `_StreamingMeshMinimumLOD` | `0` | = | `2` |
| `_StreamingMeshletMinimumLOD` | `0` | = | `2` |
| `_MeshStreamingSize` | `512` | = | `1536` |
| `_Use16bitNormalBuffer` | `false` | = | = |
| `_LodBiasSpeedTree` | `0` | = | = |
| `_StreamingMeshMinimumLODSpeedTree` | `2` | = | `0` |
| `_SpeedTreeWindLOD` | `true` | = | = |
| `_SpeedTreeSmallObjectCulling` | `16.0` | = | = |
| `_SpeedTreeWind_Leaf` | `0.0` | = | `100.0` |
| `_SpeedTreeWind_Branch` | `10.0` | = | `300.0` |
| `_SpeedTreeWind_Global` | `25.0` | = | `1000.0` |
| `_EnableFoliageDensityCulling` | `true` | = | `false` |
| `_GlobalDensity` | `1.0` | = | = |
| `_DensityCullingNear` | `10.0` | = | = |
| `_DensityCullingFar` | `100.0` | = | `1000.0` |
| `_TextureLoadLevelBias` | `0` | = | = |
| `_StreamingTextureLoadLevelBias` | `0` | = | `2` |
| `_EffectVolume` | `1.0` | = | = |
| `_IgnoreDOFEffectSampleMode` | `1` | = | = |
| `_DisableEffectVRS` | `true` | = | `false` |
| `_ParticleLightingResolution` | `[2] Medium` | = | = |
| `_UpscaleAlgorithm` | `[1] DLSS` | = | `[0] NONE` |
| `_UpscalingQuality` | `[5] Balanced` | = | `[0] NativeAA` |
| `_DLSSPreset` | `[0] Default` | = | = |
| `_UseResponsiveMask` | `false` | = | = |
| `_ResponsiveMaskScale` | `1.0` | = | = |
| `_UseLateResolve` | `false` | = | = |
| `_EnableTwoStepDLSS` | `true` | = | `false` |
| `_FilterImageQuality` | `0.75` | `0.85` | `1.0` |
| `_EnablePostSharpness` | `true` | = | `false` |
| `_PostSharpness` | `0.5` | `1.0` | `1.0` |
| `_MainRaymarchResolution` | `[5] OneEighth` | = | = |
| `_IBLRaymarchResolution` | `[2] OneThird` | = | = |
| `_IBLRaymarchScale` | `0.25` | = | `0.625` |
| `_IBLPartialDrawFrame` | `8` | = | `12` |
| `_MainRaymarchNum` | `64` | = | `128` |
| `_ShadowRaymarchNum` | `5` | = | `7` |
| `_ResourceOption` | `[2] SuperLow` | = | `[0] High` |
| `_UpscaleBoundaryBlendAdjuster` | `1.0` | = | `0.0` |
| `_ExpandDrawArea` | `0` | = | = |
| `_EnableGroundSwtichLodPerPatch` | `true` | = | `false` |
| `_DrawSignedDistanceField` | `false` | = | `true` |
| `_GlobalSDFUpdateOnLodDiffEnabled` | `false` | = | `true` |
| `_ShadowCastDistanceType` | `[3] NEAREST` | `[4] NEAREST_H` | `[2] NEAR` |
| `_GIQuality` | `[2] LOW` | = | = |
| `_GroundQuality` | `[3] LOWEST` | = | `[0] HIGH` |
| `_UseLowGround` | `true` | = | = |
| `_UseLowShellFur` | `true` | = | = |
| `_ShadowCastFur` | `true` | = | = |
| `_WindSimulationQuality` | `[2] OFF` | = | `[0] HIGH` |
| `_UseLowWindSimulation` | `true` | = | = |
| `_UseLowWaterSimulation` | `true` | = | = |
| `_HazeFilterStageEffectEnable` | `true` | = | = |
| `_PaniniEnable` | `true` | = | = |
| `_JobThreadNum` | `8` | = | = |
| `_DiffuseIntensityMultiplier` | `1.0` | = | = |
| `_ProbeTraceRayCount` | `32` | = | = |
| `_GrassCullingMode` | `[0] FAR` | = | = |
| `_GrassPushCollision` | `true` | = | = |
| `_MeshCullingSetting` | `[0] HIGHEST` | = | = |
| `_StreamingTextureQuality` | `[5] INVALID` | = | = |
| `_GroundSwitchLodDistanceArray` | — | = | `[]` |

### `_RayTracing`

| 字段 | Dock Default | Handheld Default | PC Lowest |
| --- | --- | --- | --- |
| `_RayTracing._Enable` | `false` | = | = |
| `_RayTracing._Quality` | `2` | = | = |
| `_RayTracing._SpecularRoughnessThresholdQuality` | `2` | = | = |
| `_RayTracing._AOSetting` | `[2] STANDARD` | = | = |
| `_RayTracing._GIEnable` | `false` | = | = |
| `_RayTracing._ReflectionEnable` | `true` | = | = |
| `_RayTracing._ShadowEnable` | `false` | = | = |
| `_RayTracing._TransparentEnable` | `false` | = | = |
| `_RayTracing._EffectVolume` | `1.0` | = | = |
| `_RayTracing._RecastRayLength` | `1.0` | = | = |
| `_RayTracing._EnableLod` | `true` | = | = |
| `_RayTracing._RecastPrimaryRays` | `false` | = | = |
| `_RayTracing._EnableCompaction` | `true` | = | = |
| `_RayTracing._EnableDeform` | `true` | = | = |
| `_RayTracing._EnableBlasGrouping` | `true` | = | = |
| `_RayTracing._MultiThread` | `true` | = | = |
| `_RayTracing._PreferOpaque` | `true` | = | = |
| `_RayTracing._PreferAlphaMask` | `false` | = | = |
| `_RayTracing._PreferShadowCast` | `true` | = | = |
| `_RayTracing._EnableRebraiding` | `true` | = | = |
| `_RayTracing._DisableReleaseBlasOnDrawDisabled` | `false` | = | = |
| `_RayTracing._EnableOverwriteLod` | `true` | = | = |
| `_RayTracing._OverwriteLod` | `7` | = | = |
| `_RayTracing._FoliageRayTracingLodOffset` | `7` | = | = |

### `_ExperimentalRayTrace`

| 字段 | Dock Default | Handheld Default | PC Lowest |
| --- | --- | --- | --- |
| `_ExperimentalRayTrace._RenderOutputID` | `15` | = | = |
| `_ExperimentalRayTrace._SmallObjectCullingFactor` | `1.0` | = | = |
| `_ExperimentalRayTrace._RaytracingMode` | `7` | = | = |
| `_ExperimentalRayTrace._LightSelection` | `0` | = | = |
| `_ExperimentalRayTrace._Spp` | `0` | = | = |
| `_ExperimentalRayTrace._Bounce` | `2` | = | = |
| `_ExperimentalRayTrace._PositionOffset` | `0.005` | = | = |
| `_ExperimentalRayTrace._UseAccumulationBuffer` | `false` | = | = |
| `_ExperimentalRayTrace._DiffuseResolution` | `0` | = | = |
| `_ExperimentalRayTrace._SpecularResolution` | `0` | = | = |
| `_ExperimentalRayTrace._DenoiserDebugView` | `0` | = | = |
| `_ExperimentalRayTrace._RayTracingResRatio` | `0.5` | = | = |
| `_ExperimentalRayTrace._MaxResolution.x` | `3840` | = | = |
| `_ExperimentalRayTrace._MaxResolution.y` | `2160` | = | = |
| `_ExperimentalRayTrace._PreallocateMaxResolution` | `false` | = | = |
| `_ExperimentalRayTrace._BvhTraversalHeatmap` | `false` | = | = |
| `_ExperimentalRayTrace._UseNewDenoiser` | `false` | = | = |
| `_ExperimentalRayTrace._FilterResult` | `true` | = | = |
| `_ExperimentalRayTrace._DenoiserVersion2022` | `true` | = | = |
| `_ExperimentalRayTrace._ModelScaler` | `0.005` | = | = |
| `_ExperimentalRayTrace._DepthRejectionThreshold` | `0.02` | = | = |
| `_ExperimentalRayTrace._DiffuseSecondaryBounce` | `false` | = | = |
| `_ExperimentalRayTrace._SpecularSecondaryBounce` | `false` | = | = |
| `_ExperimentalRayTrace._UseNoMovementDepthCompare` | `true` | = | = |
| `_ExperimentalRayTrace._NormalCompareThreshold` | `0.5` | = | = |
| `_ExperimentalRayTrace._UseDiffuseBounceIntensity` | `true` | = | = |
| `_ExperimentalRayTrace._DiffuseBounceIntensityMultipler` | `1.0` | = | = |
| `_ExperimentalRayTrace._UseSpecularBounceIntensity` | `true` | = | = |
| `_ExperimentalRayTrace._SpecularBounceIntensityMultipler` | `0.7` | = | = |
| `_ExperimentalRayTrace._UseRayTracingAO` | `false` | = | = |
| `_ExperimentalRayTrace._RayTracingAODistance` | `1.0` | = | = |
| `_ExperimentalRayTrace._SurfelSampling` | `false` | = | = |
| `_ExperimentalRayTrace._SurfelSize` | `0.1` | = | = |
| `_ExperimentalRayTrace._SurfelRejectDepthThreshold` | `60.0` | = | = |
| `_ExperimentalRayTrace._SpecularRoughnessThreshold` | `0.3` | = | = |
| `_ExperimentalRayTrace._UseAlphaTest` | `false` | = | = |
| `_ExperimentalRayTrace._OffsetRayOriginByStencil` | `true` | = | = |
| `_ExperimentalRayTrace._UseGBufferNormal` | `2` | = | = |
| `_ExperimentalRayTrace._UseNormalWeight` | `2` | = | = |
| `_ExperimentalRayTrace._MaxGIHistory` | `64.0` | = | = |
| `_ExperimentalRayTrace._MaxReflectionHistory` | `32.0` | = | = |
| `_ExperimentalRayTrace._GIHistoryThreshold` | `32.0` | = | = |
| `_ExperimentalRayTrace._GIFilterCenterWeight` | `16.0` | = | = |
| `_ExperimentalRayTrace._SpecularFilterIgnoreID` | `true` | = | = |
| `_ExperimentalRayTrace._MedianFilterStepSize` | `2` | = | = |
| `_ExperimentalRayTrace._HeatmapMode` | `1` | = | = |
| `_ExperimentalRayTrace._HeatmapMaxIntersectionCount` | `100` | = | = |
| `_ExperimentalRayTrace._EnableSpectralRendering` | `false` | = | = |
| `_ExperimentalRayTrace._CausticsBoost` | `1.0` | = | = |
| `_ExperimentalRayTrace._PhotonBounce` | `2` | = | = |
| `_ExperimentalRayTrace._BlurStrength` | `0.0` | = | = |
| `_ExperimentalRayTrace._TemporarlUpdateRatio` | `0.0` | = | = |
| `_ExperimentalRayTrace._EmitKiloCount` | `0` | = | = |
| `_ExperimentalRayTrace._StoreMinimumRoughness` | `0.0` | = | = |
| `_ExperimentalRayTrace._ReflectMaximumRoughness` | `0.0` | = | = |
| `_ExperimentalRayTrace._TransparentRefractionOnly` | `false` | = | = |
| `_ExperimentalRayTrace._NoColorClipReprojection` | `true` | = | = |
| `_ExperimentalRayTrace._AggressiveAccumulateData` | `false` | = | = |
| `_ExperimentalRayTrace._UseLinearColorBlend` | `false` | = | = |
| `_ExperimentalRayTrace._ReflectionUseProbeResult` | `false` | = | = |
| `_ExperimentalRayTrace._UsePathGuiding` | `false` | = | = |
| `_ExperimentalRayTrace._UseVFX` | `false` | = | = |
| `_ExperimentalRayTrace._VFXDisableNoise` | `false` | = | = |
| `_ExperimentalRayTrace._VFXSpecularDenoiserFull` | `false` | = | = |
| `_ExperimentalRayTrace._VFXSpecularDenoiserMedian` | `true` | = | = |
| `_ExperimentalRayTrace._VFXSpecularDenoiserSpatial` | `true` | = | = |
| `_ExperimentalRayTrace._VFXSpecularDenoiserGaussianNum` | `0` | = | = |
| `_ExperimentalRayTrace._VFXSpecularDenoiserTemporal` | `true` | = | = |
| `_ExperimentalRayTrace._VFXMedianFilter` | `2` | = | = |
| `_ExperimentalRayTrace._VFXRayTracingDiffuseResRatio` | `0` | = | = |
| `_ExperimentalRayTrace._VFXRayTracingSpecularResRatio` | `0` | = | = |
| `_ExperimentalRayTrace._VFXDiffuseBoost` | `1.0` | = | = |
| `_ExperimentalRayTrace._VFXSpecularBoost` | `1.0` | = | = |
| `_ExperimentalRayTrace._VFXSpecularMipBias` | `2` | = | = |
| `_ExperimentalRayTrace._VFXParticleCulling` | `true` | = | = |
| `_ExperimentalRayTrace._VFXParticleCullingAngle` | `2.5` | = | = |
| `_ExperimentalRayTrace._VFXTemporalCompositeRate` | `0.5` | = | = |
| `_ExperimentalRayTrace._VFXInvalidateTemporalRatio` | `0.02` | = | = |
| `_ExperimentalRayTrace._VFXShadowType` | `0` | = | = |
| `_ExperimentalRayTrace._AllowNoSpecular` | `false` | = | = |
| `_ExperimentalRayTrace._UseTransparent` | `true` | = | = |
| `_ExperimentalRayTrace._TransparentMultiplier` | `1.0` | = | = |
| `_ExperimentalRayTrace._TransparentResolution` | `1` | = | = |
| `_ExperimentalRayTrace._DiffuseRayLength` | `0.0` | = | = |
| `_ExperimentalRayTrace._SpecularRayLength` | `150.0` | = | = |
| `_ExperimentalRayTrace._IBLBoost` | `1.0` | = | = |
| `_ExperimentalRayTrace._FakeIBLCubemap` | `""` | = | = |
| `_ExperimentalRayTrace._UseSolidAngleCulling` | `true` | = | = |
| `_ExperimentalRayTrace._SolidAngleCullingThreshold` | `5.0` | = | = |
| `_ExperimentalRayTrace._UseFrustumCulling` | `true` | = | = |
| `_ExperimentalRayTrace._FrustumFarPlane` | `150.0` | = | = |
| `_ExperimentalRayTrace._FrustumMaxExpand` | `60.0` | = | `70.0` |
| `_ExperimentalRayTrace._LocalCubeMap` | `false` | = | = |
| `_ExperimentalRayTrace._TransparentMaskEnabled` | `false` | = | = |
| `_ExperimentalRayTrace._EnableMemoryAggressiveDiscard` | `true` | = | = |
| `_ExperimentalRayTrace._LegacyRebuildMethod` | `false` | = | = |

### `_GroundSwitchLodDistanceArray`

| 字段 | Dock Default | Handheld Default | PC Lowest |
| --- | --- | --- | --- |
| `_GroundSwitchLodDistanceArray.ST101._StageID_Fixed` | `[-1226157568] ST101` | = | — |
| `_GroundSwitchLodDistanceArray.ST101._LOD0` | `120.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST101._LOD1` | `90.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST102._StageID_Fixed` | `[-859829056] ST102` | = | — |
| `_GroundSwitchLodDistanceArray.ST102._LOD0` | `120.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST102._LOD1` | `90.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST103._StageID_Fixed` | `[-1251081216] ST103` | = | — |
| `_GroundSwitchLodDistanceArray.ST103._LOD0` | `120.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST103._LOD1` | `90.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST104._StageID_Fixed` | `[1182228864] ST104` | = | — |
| `_GroundSwitchLodDistanceArray.ST104._LOD0` | `120.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST104._LOD1` | `90.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST105._StageID_Fixed` | `[327401792] ST105` | = | — |
| `_GroundSwitchLodDistanceArray.ST105._LOD0` | `120.0` | = | — |
| `_GroundSwitchLodDistanceArray.ST105._LOD1` | `90.0` | = | — |

## 用途切换时所有发生变化的字段

每个用途与同平台 `Default` 对照。字段名与上一节的完整表一致。平台和用途标识由各小节标题给出。

### NSW2 CharMake (1)

| 字段 | 同平台 Default | CharMake |
| --- | --- | --- |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[0] DISABLE` |

### NSW2 CutScene (2)

| 字段 | 同平台 Default | CutScene |
| --- | --- | --- |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[0] DISABLE` |
| `_UpscalingQuality` | `[5] Balanced` | `[2] UltraQuality` |
| `_FilterImageQuality` | `0.75` | `0.755` |
| `_PostSharpness` | `0.5` | `0.25` |

### NSW2 Default_Fast (6)

| 字段 | 同平台 Default | Default_Fast |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[2] STANDARD` |
| `_SSR_ResolvePoint` | `[1] SSRResolvePointNum_2` | `[0] SSRResolvePointNum_1` |
| `_VolumetricFogControl_TextureSize` | `[2] W96xH54xD32` | `[4] W54xH30xD32` |
| `_VolumetricFogControl_CustomMaterialImproveNoise` | `true` | `false` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[11] TARGET_40_LOW` |
| `_SSR_Enable` | `true` | `false` |
| `_SSSSS_Enable` | `true` | `false` |
| `_MotionBlur_Enable` | `true` | `false` |
| `_FilterImageQuality` | `0.75` | `0.85` |

### NSW2 CharMake_Fast (7)

| 字段 | 同平台 Default | CharMake_Fast |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[2] STANDARD` |
| `_SSR_ResolvePoint` | `[1] SSRResolvePointNum_2` | `[0] SSRResolvePointNum_1` |
| `_VolumetricFogControl_TextureSize` | `[2] W96xH54xD32` | `[4] W54xH30xD32` |
| `_VolumetricFogControl_CustomMaterialImproveNoise` | `true` | `false` |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[0] DISABLE` |
| `_SSR_Enable` | `true` | `false` |
| `_MotionBlur_Enable` | `true` | `false` |
| `_FilterImageQuality` | `0.75` | `0.85` |

### NSW2 CutScene_Fast (8)

| 字段 | 同平台 Default | CutScene_Fast |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[2] STANDARD` |
| `_SSR_ResolvePoint` | `[1] SSRResolvePointNum_2` | `[0] SSRResolvePointNum_1` |
| `_VolumetricFogControl_TextureSize` | `[2] W96xH54xD32` | `[4] W54xH30xD32` |
| `_VolumetricFogControl_CustomMaterialImproveNoise` | `true` | `false` |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[0] DISABLE` |
| `_SSR_Enable` | `true` | `false` |
| `_MotionBlur_Enable` | `true` | `false` |
| `_UpscalingQuality` | `[5] Balanced` | `[2] UltraQuality` |
| `_FilterImageQuality` | `0.75` | `0.755` |
| `_PostSharpness` | `0.5` | `0.25` |

### NSW2 FastLoadMode (241)

| 字段 | 同平台 Default | FastLoadMode |
| --- | --- | --- |
| `_ImageQualityRate` | `1.0` | `0.1` |
| `_AntiAliasing` | `[1] TAA` | `[4] NONE` |
| `_SharpnessSetting` | `4` | `1` |
| `_DownsamplerSetting` | `1` | `0` |
| `_ShadowQuality` | `[3] HIGH` | `[0] LOWEST` |
| `_AOSetting` | `[1] LOW` | `[0] LOWEST` |
| `_SSR_ResolvePoint` | `[1] SSRResolvePointNum_2` | `[0] SSRResolvePointNum_1` |
| `_VolumetricFogControl_TextureSize` | `[2] W96xH54xD32` | `[4] W54xH30xD32` |
| `_VolumetricFogControl_CustomMaterialImproveNoise` | `true` | `false` |
| `_ContactShadowSetting` | `[2] CUSTOM` | `[0] OFF` |
| `_MeshletSmallObjectCulling` | `12.0` | `65535.0` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[0] DISABLE` |
| `_AutomaticSamplerQuality` | `0` | `3` |
| `_SecondaryAutomaticSamplerQuality` | `0` | `3` |
| `_DynamicShadowEnable` | `true` | `false` |
| `_Bloom_Enable` | `true` | `false` |
| `_Bloom_ReductionLevel` | `3` | `2` |
| `_DOF_Enable` | `true` | `false` |
| `_SSR_Enable` | `true` | `false` |
| `_SSSSS_Enable` | `true` | `false` |
| `_Fog_Enable` | `true` | `false` |
| `_VolumetricFogControl_Enable` | `true` | `false` |
| `_MotionBlur_Enable` | `true` | `false` |
| `_FilmGrain_Enable` | `true` | `false` |
| `_LensFlare_Enable` | `true` | `false` |
| `_GodRay_Enable` | `true` | `false` |
| `_LensDistortionSetting` | `0` | `2` |
| `_LocalExposureBlurredLogDownsampleSize` | `2` | `0` |
| `_LodBiasSpeedTree` | `0` | `1` |
| `_SpeedTreeSmallObjectCulling` | `16.0` | `65535.0` |
| `_UpscaleAlgorithm` | `[1] DLSS` | `[0] NONE` |
| `_UpscalingQuality` | `[5] Balanced` | `[7] MaxPerformance` |
| `_EnableTwoStepDLSS` | `true` | `false` |
| `_FilterImageQuality` | `0.75` | `0.85` |
| `_PostSharpness` | `0.5` | `1.0` |
| `_ExperimentalRayTrace._DiffuseResolution` | `0` | `1` |
| `_ExperimentalRayTrace._SpecularResolution` | `0` | `1` |
| `_ExperimentalRayTrace._RayTracingResRatio` | `0.5` | `1.0` |
| `_ExperimentalRayTrace._DepthRejectionThreshold` | `0.02` | `0.01` |
| `_ExperimentalRayTrace._DiffuseSecondaryBounce` | `false` | `true` |
| `_ExperimentalRayTrace._SpecularSecondaryBounce` | `false` | `true` |
| `_ExperimentalRayTrace._SpecularBounceIntensityMultipler` | `0.7` | `1.0` |
| `_ExperimentalRayTrace._UseRayTracingAO` | `false` | `true` |
| `_ExperimentalRayTrace._RayTracingAODistance` | `1.0` | `4.0` |
| `_ExperimentalRayTrace._UseAlphaTest` | `false` | `true` |
| `_ExperimentalRayTrace._MedianFilterStepSize` | `2` | `1` |
| `_ExperimentalRayTrace._TransparentResolution` | `1` | `2` |
| `_ExperimentalRayTrace._DiffuseRayLength` | `0.0` | `1000.0` |
| `_ExperimentalRayTrace._SpecularRayLength` | `150.0` | `1000.0` |
| `_ExperimentalRayTrace._SolidAngleCullingThreshold` | `5.0` | `2.5` |
| `_ExperimentalRayTrace._FrustumFarPlane` | `150.0` | `1000000000.0` |
| `_ExperimentalRayTrace._FrustumMaxExpand` | `60.0` | `100.0` |
| `_HazeFilterStageEffectEnable` | `true` | `false` |
| `_JobThreadNum` | `8` | `0` |

### NSW2 DialoguePlaying (242)

| 字段 | 同平台 Default | DialoguePlaying |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[5] NONE` |
| `_DynamicResolutionMode` | `[12] TARGET_30_LOW_D` | `[0] DISABLE` |

### NSW2_HANDHELD CharMake (1)

| 字段 | 同平台 Default | CharMake |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[2] STANDARD` |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_DynamicResolutionMode` | `[10] TARGET_30_LOW` | `[0] DISABLE` |
| `_SSSSS_Enable` | `false` | `true` |
| `_ShadowCastDistanceType` | `[4] NEAREST_H` | `[3] NEAREST` |

### NSW2_HANDHELD CutScene (2)

| 字段 | 同平台 Default | CutScene |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[2] STANDARD` |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_DynamicResolutionMode` | `[10] TARGET_30_LOW` | `[0] DISABLE` |
| `_SSSSS_Enable` | `false` | `true` |
| `_UpscalingQuality` | `[5] Balanced` | `[2] UltraQuality` |
| `_FilterImageQuality` | `0.85` | `0.755` |
| `_PostSharpness` | `1.0` | `0.25` |
| `_ShadowCastDistanceType` | `[4] NEAREST_H` | `[3] NEAREST` |

### NSW2_HANDHELD DialoguePlaying (242)

| 字段 | 同平台 Default | DialoguePlaying |
| --- | --- | --- |
| `_ShadowQuality` | `[3] HIGH` | `[2] STANDARD` |
| `_TemporalBlendSDFShadow` | `false` | `true` |
| `_SSSSS_Enable` | `false` | `true` |
| `_ShadowCastDistanceType` | `[4] NEAREST_H` | `[3] NEAREST` |

## 动态分辨率

键由图形预设的 `_DynamicResolutionMode` 指向同文件的 `_DynamicResolutionParamList._Mode`。三条 NSW2 用到的记录各有六个 `[0.0, 0.0]` 的 `_ManualResolution` 向量。

| Mode | 用途 | MinImageQuality | ResolutionLevels | UpTime / DownTime | UpFrameWait / DownFrameWait | RenderWaitTimeThreshold |
| --- | --- | --- | --- | --- | --- | --- |
| `[10] TARGET_30_LOW` | Handheld Default、DialoguePlaying | `0.5` | `2` | 32.0 / 33.4 | 4 / 4 | `0.1` |
| `[11] TARGET_40_LOW` | Dock Default_Fast | `0.5` | `2` | 23.5 / 25.0 | 4 / 4 | `0.1` |
| `[12] TARGET_30_LOW_D` | Dock Default | `0.5` | `5` | 31.0 / 33.4 | 4 / 4 | `0.1` |

## 纹理与网格流式加载

源文件同为 `GraphicsPreset.user.3.json`。根对象按品质或显存阈值提供共用数据。两个 NSW2 Default 的 `_StreamingTextureQuality` 都是 `[5] INVALID`，所以仅凭这两行无法定位以下五档中的最终选择。

### 纹理流式档位

`_StreamingTextureSettingList`

| `_Quality` | `_StreamingTextureLoadLevelBias` | `_StreamingBudgetSizeMB` | `_BreadthFirstStreaming` | `_BreadthFirstShortcutResolution` | `_VramBudgetLimitResolution` | `_OutOfViewTextureStreamingResolution` | `_MinimumStreamingTextureResolution` | `_MaximumStreamingTextureResolution` | `_ClosestStreamingTextureDistance` | `_ClosestMaximumStreamingTextureResolution` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[0] LOWEST` | `2` | `350` | `true` | `[5] StreamingTextureResolution_256` | `[5] StreamingTextureResolution_256` | `[5] MPMROOVTextureResolution_256` | `[5] MinimumStreamingTextureResoltuion_256` | `[4] MaximumStreamingTextureResolution_512` | `0.0` | `[4] MaximumStreamingTextureResolution_512` |
| `[1] LOW` | `1` | `512` | `true` | `[5] StreamingTextureResolution_256` | `[5] StreamingTextureResolution_256` | `[5] MPMROOVTextureResolution_256` | `[5] MinimumStreamingTextureResoltuion_256` | `[4] MaximumStreamingTextureResolution_512` | `0.0` | `[4] MaximumStreamingTextureResolution_512` |
| `[2] STANDARD` | `1` | `1024` | `true` | `[4] StreamingTextureResolution_512` | `[4] StreamingTextureResolution_512` | `[4] MPMROOVTextureResolution_512` | `[4] MinimumStreamingTextureResoltuion_512` | `[3] MaximumStreamingTextureResolution_1024` | `0.0` | `[3] MaximumStreamingTextureResolution_1024` |
| `[3] HIGH` | `0` | `2048` | `true` | `[4] StreamingTextureResolution_512` | `[4] StreamingTextureResolution_512` | `[4] MPMROOVTextureResolution_512` | `[4] MinimumStreamingTextureResoltuion_512` | `[2] MaximumStreamingTextureResolution_2048` | `0.0` | `[2] MaximumStreamingTextureResolution_2048` |
| `[4] HIGHEST` | `0` | `3072` | `true` | `[4] StreamingTextureResolution_512` | `[4] StreamingTextureResolution_512` | `[4] MPMROOVTextureResolution_512` | `[4] MinimumStreamingTextureResoltuion_512` | `[1] MaximumStreamingTextureResolution_4096` | `0.0` | `[1] MaximumStreamingTextureResolution_4096` |

### 纹理预算最大值

`_StreamingTextureLimitList`

| `_VRAMThresholdSizeMB` | `_StreamingBudgetLimitSizeMB` |
| --- | --- |
| `0` | `512` |
| `7000` | `1024` |
| `10000` | `1792` |
| `13000` | `3072` |
| `17000` | `4096` |

### 网格流式档位和显存阈值

`_StreamingMeshLimitList`

| `_MeshQuality` | `_StreamingMeshMinimumLodLimit` | `_StreamingMeshletMinimumLodLimit` | `_DownVramThresholdMB` | `_UpVramThresholdMB` |
| --- | --- | --- | --- | --- |
| `0` | `0` | `0` | `500` | `0` |
| `0` | `0` | `1` | `600` | `450` |
| `0` | `1` | `1` | `700` | `550` |
| `0` | `1` | `2` | `800` | `650` |
| `0` | `2` | `2` | `0` | `750` |
| `1` | `1` | `1` | `500` | `0` |
| `1` | `1` | `2` | `600` | `450` |
| `1` | `2` | `2` | `0` | `550` |
| `2` | `2` | `2` | `0` | `0` |
| `3` | `2` | `1` | `200` | `0` |
| `3` | `2` | `2` | `0` | `170` |
| `4` | `0` | `2` | `210` | `0` |
| `4` | `1` | `2` | `0` | `180` |

两个 NSW2 Default 写入 `_MeshQuality = 2`、`_MeshStreamingSize = 512` 与两个最小 LOD 字段 `0 / 0`。根表的 `_MeshQuality = 2` 行另含 `2 / 2` 的 LOD 限制。二者属于不同字段和结构，需追踪加载与覆盖顺序才可得出运行时最终 LOD。

### 通常状态与事件播放时的资源保护

源文件为 `natives/STM/System/SystemSetting/AppStreamingControllerManagerSetting.user.3.json`，行来自 `_PlatformData`。此文件的 `[5] NSW2` 与 GraphicsPreset 的 14、15 使用不同的枚举。它只定义一个 NSW2 项。

| 平台 | 状态 | 键 | 保护距离 | Mip 级别 | LOD 级别 | 基础视野 | 淡入淡出期间预加载距离 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `[1] PC` | 通常 | `_ProtectData` | `10.0` | `2` | `2` | `40.0` | `64.0` |
| `[1] PC` | 通常 | `_ProtectData` | `20.0` | `3` | `4` | `40.0` | `64.0` |
| `[1] PC` | 事件播放 | `_ProtectDataEventPlaying` | `10.0` | `2` | `2` | `40.0` | `64.0` |
| `[1] PC` | 事件播放 | `_ProtectDataEventPlaying` | `30.0` | `3` | `4` | `40.0` | `64.0` |
| `[5] NSW2` | 通常 | `_ProtectData` | `10.0` | `1` | `1` | `40.0` | `64.0` |
| `[5] NSW2` | 通常 | `_ProtectData` | `20.0` | `2` | `2` | `40.0` | `64.0` |
| `[5] NSW2` | 事件播放 | `_ProtectDataEventPlaying` | `10.0` | `1` | `1` | `40.0` | `64.0` |
| `[5] NSW2` | 事件播放 | `_ProtectDataEventPlaying` | `30.0` | `2` | `2` | `40.0` | `64.0` |

## 阴影距离与全局光照

共用根表 `_ShadowDistanceSettings` 按 `_ShadowCastDistanceType` 查找。阵列保留原顺序，其中未启用级联的条目不直接代表可见阴影距离。

| `_Type` | `_CascadeNum` | `_DynamicShadowCascadeRange` | `_WorldPartition` | `_CullingScaler` |
| --- | --- | --- | --- | --- |
| `[0] FAR` | `3` | `3` | `[2.0, 10.0, 30.0, 100.0]` | `[1.0, 1.0, 2.0, 4.0]` |
| `[1] MIDDLE` | `3` | `3` | `[2.0, 8.0, 25.0, 100.0]` | `[1.0, 1.0, 2.0, 4.0]` |
| `[2] NEAR` | `2` | `2` | `[6.0, 25.0, 25.0, 100.0]` | `[1.0, 1.0, 2.0, 4.0]` |
| `[3] NEAREST` | `2` | `2` | `[6.0, 20.0, 30.0, 40.0]` | `[1.0, 1.0, 2.0, 4.0]` |
| `[4] NEAREST_H` | `1` | `1` | `[20.0, 20.0, 50.0, 100.0]` | `[1.0, 1.0, 2.0, 4.0]` |

两个 NSW2 Default 的 GI 品质为 `[2] LOW`，照明模式为 `[2] DynamicProbe`。下表区分根表 `_GIQualitySettings` 的 `_Type = 2` 行与两份预设自带的同名字段。根表的探针配置不能直接替换预设值。

| 字段 | GI 根表 LOW | Dock / Handheld Default 同名字段 |
| --- | --- | --- |
| `_TemporalAccumulation` | `2` | — |
| `_ScreenSpecular` | `2` | — |
| `_NoProbe` | `2` | — |
| `_ProbeLightBlock` | `1` | — |
| `_VoxelResolution` | `0` | — |
| `_VoxelSize` | `1.0` | — |
| `_ProbeVolumeMin` | `2` | — |
| `_ProbeRelocateFarLimitScale` | `0.8` | — |
| `_ProbeRadianceResolution` | `1` | — |
| `_ProbeForceUpdate` | `1` | — |
| `_ProbeResidentDistance` | `1` | — |
| `_ProbeResidentForceUpdate` | `1` | — |
| `_ProbeDistancePrecision` | `1` | — |
| `_TransparentProbeVolumeMin` | `3` | — |
| `_TransparentProbeRayNum` | `0` | — |
| `_TransparentProbeRadianceResolution` | `1` | — |
| `_TransparentProbeForceUpdate` | `1` | — |
| `_ScreenProbe` | `false` | — |
| `_SdfTraceThresholdScale` | `0.6` | — |
| `_GIPSurfelEllipseSampling` | `false` | — |
| `_GIPRadianceVolumeStartLodNo` | `0` | — |
| `_GlobalSDFVoxelSize` | `0.5` | — |
| `_GlobalSDFClipmapNum` | `5` | — |
| `_GlobalSDFMaxRayDistance` | `10.0` | — |
| `_GIPRadianceVolumeClipmapNum` | `6` | — |
| `_GIPRadianceVolumeBaseGridSize` | `4.0` | — |
| `_GIPRadianceVolumeResolution` | `8` | — |
| `_BreakingPBRCubemapReflectionScale` | `1.0` | — |
| `_GIPointCloudMinLod` | `0` | `1` |
| `_GIPointCloudLodBias` | `0.0` | — |
| `_GIPointCloudRadianceVolumeClipmapNum` | `6` | — |
| `_GIPointCloudRadianceVolumeBaseGridSize` | `4.0` | — |
| `_GIPointCloudRadianceVolumeResolution` | `8` | — |
| `_ProbeTraceRayCount` | `16` | `32` |
| `_ProbeTraceUpdateDivisionType` | `[1] Normal` | `8` |
| `_ProbeTraceAccumulationWeight` | `0.975` | `0.0` |
| `_ProbeTraceRayAccumulationFrame` | `1` | `8` |
| `_OutdoorLightProbeMeshNormalWarpingScale` | `0.25` | — |
| `_OutdoorLightProbeGSDFGradientNormalWarpingScale` | `0.5` | — |
| `_OutdoorLightProbeWarpingBlendRate` | `0.5` | — |
| `_OutdoorLightProbeSH2CustomCoeffL0` | `0.3304` | — |
| `_OutdoorLightProbeSH2CustomCoeffL1` | `0.4566` | — |
| `_OutdoorLightProbeSH2CustomCoeffL2` | `0.213` | — |
| `_OutdoorLightProbeTranslucentBoost` | `0.7` | — |

## 草地全局与场景剔除

源文件为 `natives/STM/System/SystemSetting/GrassCullingSetting.user.3.json`，下表为 Steam 原始值。两份 NSW2 Default 的普通枚举选 `[0] FAR`，在此表对应固定枚举 `[6601] FAR`。NSW2 直接使用预设的全局密度和近远裁剪，PC 通过这张表按关卡与档位写入同一组参数，详见[平台资源对照](platform-resources.md)。根部的 `_EnableDensityCulling` 和 `_EnableDensityCullingConsoleTarget` 均为真。

| 层级 | 场景 | 剔除档 | `_BaseScale` | `_RangeStart` | `_RangeAnimation` | `_EffectiveRangeY` | `_EffectiveAnimationRangeY` | `_GlobalDensity` | `_DensityCullingNear` | `_DensityCullingFar` | `_DensityCullingAttenuationExponent` | `_DensityCullingHeightRangeMin` | `_DensityCullingHeightRangeMax` | `_DensityCullingHeightFadeDistance` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `_Data` | 通用 | `6601 FAR` | `1.0` | `50.0` | `30.0` | `20.0` | `10.0` | `1.0` | `30.0` | `600.0` | `1.0` | `20.0` | `20.0` | `10.0` |
| `_Data` | 通用 | `20827 MIDDLE` | `0.9` | `40.0` | `20.0` | `20.0` | `10.0` | `1.0` | `30.0` | `600.0` | `3.0` | `20.0` | `20.0` | `10.0` |
| `_Data` | 通用 | `8922 NEAR` | `0.75` | `30.0` | `20.0` | `20.0` | `10.0` | `0.9` | `30.0` | `600.0` | `1.0` | `20.0` | `20.0` | `10.0` |
| `_Data` | 通用 | `24229 NEAREST` | `1.0` | `30.0` | `20.0` | `20.0` | `10.0` | `0.9` | `30.0` | `400.0` | `2.0` | `20.0` | `20.0` | `10.0` |
| `_StageData` | `[-1226157568] ST101` | `6601 FAR` | `1.0` | `90.0` | `20.0` | `10.0` | `10.0` | `1.0` | `0.0` | `600.0` | `1.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-1226157568] ST101` | `20827 MIDDLE` | `0.9` | `30.0` | `20.0` | `10.0` | `10.0` | `1.0` | `0.0` | `600.0` | `3.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-1226157568] ST101` | `8922 NEAR` | `0.75` | `20.0` | `10.0` | `10.0` | `10.0` | `0.8` | `0.0` | `600.0` | `1.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-1226157568] ST101` | `24229 NEAREST` | `1.0` | `30.0` | `20.0` | `20.0` | `10.0` | `0.8` | `0.0` | `400.0` | `2.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-859829056] ST102` | `6601 FAR` | `1.0` | `30.0` | `30.0` | `20.0` | `10.0` | `1.0` | `30.0` | `600.0` | `1.0` | `20.0` | `20.0` | `10.0` |
| `_StageData` | `[-859829056] ST102` | `20827 MIDDLE` | `0.9` | `25.0` | `20.0` | `20.0` | `10.0` | `1.0` | `30.0` | `600.0` | `3.0` | `20.0` | `20.0` | `10.0` |
| `_StageData` | `[-859829056] ST102` | `8922 NEAR` | `0.75` | `20.0` | `15.0` | `20.0` | `10.0` | `0.9` | `30.0` | `600.0` | `1.0` | `20.0` | `20.0` | `10.0` |
| `_StageData` | `[-859829056] ST102` | `24229 NEAREST` | `1.0` | `30.0` | `20.0` | `20.0` | `10.0` | `0.9` | `30.0` | `400.0` | `2.0` | `20.0` | `20.0` | `10.0` |
| `_StageData` | `[-1251081216] ST103` | `6601 FAR` | `1.0` | `90.0` | `20.0` | `10.0` | `10.0` | `1.0` | `30.0` | `600.0` | `1.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-1251081216] ST103` | `20827 MIDDLE` | `0.9` | `30.0` | `20.0` | `10.0` | `10.0` | `1.0` | `30.0` | `600.0` | `3.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-1251081216] ST103` | `8922 NEAR` | `0.75` | `20.0` | `10.0` | `10.0` | `10.0` | `0.9` | `30.0` | `600.0` | `1.0` | `10.0` | `10.0` | `10.0` |
| `_StageData` | `[-1251081216] ST103` | `24229 NEAREST` | `1.0` | `30.0` | `20.0` | `20.0` | `10.0` | `0.9` | `30.0` | `400.0` | `2.0` | `10.0` | `10.0` | `10.0` |

## PC 最低档菜单查表

源文件位于 `natives/STM/GameDesign/Common/Option`。选择 `OptionGraphicsPresetData._Settings._Quality = [4] LOWEST` 指定菜单选项。对应 `OptionGraphicsData._Items` 项才给出运行时数值或多字段载荷。选项编号和引擎字段值可不同，例如最低档的抗锯齿编号 `2` 指向实际 `[4] NONE`。

| PC 最低档字段 | 选项编号 | 菜单项 | 菜单载荷字段 |
| --- | --- | --- | --- |
| `_AntiAliasing` | `2` | `[2] NONE` | `_Value` `[4] NONE` |
| `_TextureQuality` | `4` | `[4] LOWEST` | `_StreamingTextureQuality` `[4] LOWEST` / `_ValueNoDlc` `3` / `_ValueDlcAvailable` `4` |
| `_TextureFilter` | `5` | `[5] BILINEAR` | `_Value` `[0] Bilinear` |
| `_MeshQuality` | `2` | `[2] STANDARD` | `_Value` `2` |
| `_SkyCloudQuality` | `3` | `[3] LOW` | `_MainRaymarchResolution` `[4] OneFifth` / `_IBLRaymarchResolution` `[2] OneThird` / `_IBLRaymarchScale` `0.75` / `_IBLPartialDrawFrame` `10` / `_MainRaymarchNum` `128` / `_ShadowRaymarchNum` `7` / `_ResourceOption` `[0] High` / `_UpscaleBoundaryBlendAdjuster` `0.0` |
| `_PlantQuality` | `2` | `[2] LOW` | `_Value` `2` |
| `_PlantShaking` | `1` | `[1] OFF` | `_Leaf` `0.0` / `_Branch` `0.0` / `_Global` `0.0` |
| `_PlantDensity` | `3` | `[3] LOWEST` | `_Value` `[3] NEAREST` |
| `_PlantCollision` | `1` | `[1] OFF` | `_Value` `1` |
| `_ShadowQuality` | `4` | `[4] LOWEST` | `_Value` `[0] LOWEST` |
| `_ContactShadow` | `1` | `[1] OFF` | `_Value` `[0] OFF` |
| `_AmbientOcclusion` | `2` | `[2] OFF` | `_AOSetting` `[0] LOWEST` / `_SSAO_HalfResolution` `false` |
| `_Bloom` | `1` | `[1] LOW` | `_Enable` `true` / `_ReductionLevel` `2` |
| `_ScreenSpaceReflection` | `1` | — | 独立开关，未出现在这份菜单映射表 |
| `_SsssScattering` | `1` | — | 独立开关，未出现在这份菜单映射表 |
| `_DepthOfField` | `1` | — | 独立开关，未出现在这份菜单映射表 |
| `_VolumeFogQuality` | `4` | `[4] LOWEST` | `_Value` `[4] W54xH30xD32` / `_ShadowCullingBlendFactorScale` `1.0` / `_CustomMaterialImproveNoise` `false` |
| `_VariableRateShading` | `0` | `[0] OFF` | `_Value` `[0] Off` |
| `_FurQuality` | `1` | `[1] LOW` | `_Value` `true` |
| `_WindFluidSimulation` | `2` | `[2] OFF` | `_Value` `[2] OFF` |
| `_WaterFluidEffect` | `1` | `[1] DISABLE` | `_Value` `true` |
| `_DistantShadow` | `1` | `[1] LOW` | `_Value` `true` |
| `_ShadowCastDistance` | `2` | `[2] NEAR` | `_Value` `[2] NEAR` |
| `_AmbientLight` | `2` | `[2] LOW` | `_Value` `[2] LOW` |

| PC 最低档的独立表 | 选中项 |
| --- | --- |
| `_UpscaleMode` | `_Value` `[4] ULTRA_PERFORMANCE` |
| `_GroundQuality` | `_Value` `[2] LOW` |
| `_SandSnowWaterQuality` | `_Value` `[4] LOWEST` |
| `_CullingSettings` | `_Value` `[3] LOW` / `_SmallObjectCulling` `8.0` / `_MPMRSmallObjectCullingResolution` `[720] MPMRSmallObjectCullingResolution_720p` |

菜单载荷的值适用于选择该项的现有档位或自定义配置。例如天空/云 `[3] LOW` 使用五分之一分辨率进行主光线步进，两份 NSW2 Default 使用八分之一。草地密度 `[3] LOWEST` 对应 `NEAREST`，两份 NSW2 Default 均为 `FAR`。地面、沙雪水和剔除独立表分别提供每个预设自己的行。

本地 2026-10-27 的 `MonsterHunterWilds_dump.exe` 和 `il2cpp_dump.json` 给出了菜单应用路径。`app.cGUISystemModuleOption.applyGraphicsPresetSetting` 位于 `0x145D1E230`。该函数取对象 `+0x48` 的 `_OptionGraphicsPresetData`，再读取资源对象 `+0x20` 的 `_Settings`，按画质枚举取行。它遍历该行的选项数组，对 `setOptionValue`（`0x145A1E390`）确认发生变化的条目调用 `applySetting`（`0x145D1D260`）。这条路径解释了为什么总体预设可以重新应用独立的菜单项。

同一函数还从资源对象 `+0x28` 取 `_UpscaleMode`，将所选行的值应用到选项编号 `234`（`UPSCALE_MODE`）。当前上采样类型为 `NONE` 时跳过这一步，分支判断位于 `0x145D1E314`，使用选项编号 `232`（`UPSCALE_TYPE`）与类型值 `3`。因此上采样类型和上采样质量分别受各自的条件和表项控制。
