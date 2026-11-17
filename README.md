<h1 align="center">MHWS NS2 Graphics Preset for PC</h1>

<p align="center">Use the Nintendo Switch 2 graphics presets in Monster Hunter Wilds on PC.</p>

<p align="center">
  <a href="https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/latest"><img src="https://img.shields.io/github/v/release/dzxrly/MHWS-NS2-Graphics-Preset-for-PC?display_name=tag&amp;logo=github" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/dzxrly/MHWS-NS2-Graphics-Preset-for-PC" alt="MIT license"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="docs/README.zh-CN.md">简体中文</a> · <a href="docs/README.zh-TW.md">繁體中文</a>
</p>

<div align="center">
  <a href="https://github.com/dzxrly/PyREUser3">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-dark.svg">
      <img alt="Powered by PyREUser3" src="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-light.svg">
    </picture>
  </a>
</div>

## Download

Choose one package. Both are based on Steam version `1.42.0.3` of Monster Hunter Wilds.

| Preset | Download |
| --- | --- |
| Dock | [Dock v1.0.2](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/download/v1.0.2/MHWS_NS2_Graphics_Preset_for_PC_Dock_v1.0.2.zip) |
| Handheld | [Handheld v1.0.2](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/download/v1.0.2/MHWS_NS2_Graphics_Preset_for_PC_Handheld_v1.0.2.zip) |

[Browse all releases](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases)

## Install

1. Download either the Dock or Handheld ZIP.
2. With the game closed, extract the ZIP and copy its `natives` folder into the game directory next to `MonsterHunterWilds.exe`. Allow it to replace files from the previous version of this mod.
3. Launch the game with [REFramework](https://github.com/praydog/REFramework) installed. If **Loose File Loader** is off, enable it and restart the game.

To switch between Dock and Handheld, repeat these steps with the other package. If you previously installed a version of this mod that used Lua, remove its old `reframework/autorun/MHWS_NSW2onPC.lua` from the game directory.

## Preset differences

| Setting | Dock | Handheld |
| --- | --- | --- |
| Screen-space reflections and skin subsurface scattering | On | Off |
| Dynamic shadow cascades | 2 | 1 |
| Volumetric fog grid | `96 × 54 × 32` | `54 × 30 × 32` |

All five PC graphics presets use the same mod settings for the selected mode. The game keeps its original menu labels and may display the first matching label when options share the same values. Handheld still uses the Switch 2 preset's `HIGH` shadow quality. Output resolution, frame rate and the available upscaling methods follow your PC settings.

If some settings from an older install or another mode persist, close the game, back up `config.ini` and move it out of the game directory. The game will create a fresh configuration on launch. Set your PC preferences, such as resolution, again afterward.
