<h1 align="center">MHWS NS2 Graphics Preset for PC</h1>

<p align="center">在 PC 版《魔物獵人 荒野》中啟用 Nintendo Switch 2 的畫質預設。</p>

<p align="center">
  <a href="https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/latest"><img src="https://img.shields.io/github/v/release/dzxrly/MHWS-NS2-Graphics-Preset-for-PC?display_name=tag&amp;logo=github" alt="最新版本"></a>
  <a href="../LICENSE"><img src="https://img.shields.io/github/license/dzxrly/MHWS-NS2-Graphics-Preset-for-PC" alt="MIT 授權條款"></a>
</p>

<p align="center">
  <a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <strong>繁體中文</strong>
</p>

## 下載

兩個安裝包皆以 Steam 版《魔物獵人 荒野》`1.42.0.3` 的遊戲資料為基礎。請擇一下載。

| 預設 | 下載 |
| --- | --- |
| 底座模式（Dock） | [底座版 v1.0.2](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/download/v1.0.2/MHWS_NS2_Graphics_Preset_for_PC_Dock_v1.0.2.zip) |
| 掌機模式（Handheld） | [掌機版 v1.0.2](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases/download/v1.0.2/MHWS_NS2_Graphics_Preset_for_PC_Handheld_v1.0.2.zip) |

[查看所有版本](https://github.com/dzxrly/MHWS-NS2-Graphics-Preset-for-PC/releases)

## 安裝

1. 關閉遊戲，下載想使用的預設壓縮檔。
2. 解壓縮後，將 `natives` 資料夾複製到 `MonsterHunterWilds.exe` 所在的遊戲目錄。首次安裝會新增這些檔案，更新時則覆蓋本模組舊版的檔案。
3. 安裝 [REFramework](https://github.com/praydog/REFramework) 後啟動遊戲。如果 **Loose File Loader** 尚未開啟，請啟用它並重新啟動遊戲。

切換底座與掌機模式時，用另一個安裝包重複上述步驟。如果安裝過本模組使用 Lua 的舊版，請移除遊戲目錄中的舊指令碼 `reframework/autorun/MHWS_NSW2onPC.lua`。

## 預設差異

| 設定 | 底座模式 | 掌機模式 |
| --- | --- | --- |
| 螢幕空間反射與皮膚次表面散射 | 開啟 | 關閉 |
| 動態陰影級聯數 | 2 | 1 |
| 體積霧網格 | `96 × 54 × 32` | `54 × 30 × 32` |

同一模式下，PC 的五檔畫質預設共用一組模組參數。遊戲保留原本的選單標籤，有多個選項共用參數時，選單可能顯示第一個符合的標籤。掌機版沿用 Switch 2 預設的 `HIGH` 陰影品質。輸出解析度、影格率和可用的超解析度技術由 PC 設定決定。

如果更新或切換模式後仍看到舊設定，請先關閉遊戲，備份 `config.ini` 並將它移出遊戲目錄。重新啟動後，遊戲會產生新的設定檔，解析度等 PC 設定需要重新調整。

<div align="center">
  <a href="https://github.com/dzxrly/PyREUser3">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-dark.svg">
      <img alt="Powered by PyREUser3" src="https://raw.githubusercontent.com/dzxrly/PyREUser3/branding/powered-by-pyreuser3-simple-light.svg">
    </picture>
  </a>
</div>
