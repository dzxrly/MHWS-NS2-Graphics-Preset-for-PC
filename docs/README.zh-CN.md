<h1 align="center">MHWS NS2 Graphics Preset for PC</h1>

<p align="center">在 PC 版《怪物猎人 荒野》中启用 Nintendo Switch 2 的画质预设。</p>

<p align="center">
  <a href="https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/latest"><img src="https://img.shields.io/github/v/release/dzxrly/MHWS-NS2-Graphics-Preset-for-PC?display_name=tag&amp;logo=github" alt="最新版本"></a>
  <a href="../LICENSE"><img src="https://img.shields.io/github/license/dzxrly/MHWS-NS2-Graphics-Preset-for-PC" alt="MIT 许可证"></a>
</p>

<p align="center">
  <a href="../README.md">English</a> · <strong>简体中文</strong> · <a href="README.zh-TW.md">繁體中文</a>
</p>

## 下载

两份安装包基于 Steam 版《怪物猎人 荒野》`1.42.0.3` 的游戏数据。请选择其中一个。

| 预设 | 下载 |
| --- | --- |
| 主机模式（Dock） | [主机版 v1.0.2](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/download/v1.0.2/MHWS_NS2_Graphics_Preset_for_PC_Dock_v1.0.2.zip) |
| 掌机模式（Handheld） | [掌机版 v1.0.2](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/download/v1.0.2/MHWS_NS2_Graphics_Preset_for_PC_Handheld_v1.0.2.zip) |

[查看所有版本](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases)

## 安装

1. 退出游戏，下载想用的预设压缩包。
2. 解压，将其中的 `natives` 目录复制到 `MonsterHunterWilds.exe` 所在的游戏目录。首次安装会添加这些文件，升级时覆盖本模组旧版的文件。
3. 安装 [REFramework](https://github.com/praydog/REFramework) 后启动游戏。如果 **Loose File Loader** 尚未开启，请启用它并重启游戏。

切换主机和掌机模式时，用另一份安装包重复上述步骤。如果装过本模组使用 Lua 的旧版，请移除游戏目录中的旧脚本 `reframework/autorun/MHWS_NSW2onPC.lua`。

## 预设差异

| 设置 | 主机模式 | 掌机模式 |
| --- | --- | --- |
| 屏幕空间反射和皮肤次表面散射 | 开 | 关 |
| 动态阴影级联数 | 2 | 1 |
| 体积雾网格 | `96 × 54 × 32` | `54 × 30 × 32` |

同一模式下，PC 的五档画质预设共用一套模组参数。游戏保留原有的菜单标签，多个选项使用相同参数时，菜单可能显示首个匹配的标签。掌机版沿用 Switch 2 预设的 `HIGH` 阴影质量。输出分辨率、帧率和可用的超分辨率方式由 PC 设置决定。

如果升级或切换模式后仍看到旧设置，请退出游戏，备份 `config.ini` 并将其移出游戏目录。重启后游戏会生成新配置，分辨率等 PC 设置需要重新调整。

<div align="center">
  <a href="https://github.com/dzxrly/PyREUser3">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-dark.svg">
      <img alt="Powered by PyREUser3" src="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-light.svg">
    </picture>
  </a>
</div>
