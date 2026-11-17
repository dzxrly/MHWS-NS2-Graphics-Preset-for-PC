# Build Data Tools

`tools/build_data.py` follows the Better4KHDTexture build-data tool, which was adapted from `dzxrly/MHST3-NormalOtomonScale`. It stores large build-only JSON files as GitHub Release assets. The copied tool is covered by the [MIT license](LICENSE).

The default build-data files are listed below.

```text
data/rszMHWS.json
data/il2cpp_dump.json
```

The `build-data` release contains these assets.

```text
rszMHWS.json.gz
rszMHWS.json.gz.sha256
il2cpp_dump.json.gz
il2cpp_dump.json.gz.sha256
```

## Upload

Install and log in to GitHub CLI.

```powershell
gh auth login
```

Then run this from the repository root.

```powershell
python tools/build_data.py upload
```

To see the compressed asset sizes and checksums without uploading, run a dry run.

```powershell
python tools/build_data.py upload --dry-run
```

To process only one file, use `--file`.

```powershell
python tools/build_data.py upload --file data/rszMHWS.json
```

## Download

GitHub Actions runs this command before building. Run the same command locally after cloning if either metadata file is missing.

```powershell
python tools/build_data.py download
```

The tool downloads each `.gz` and its matching `.sha256`, verifies the compressed assets, and unpacks the selected files before restoring them to `data/`.

## Notes

- Run `python tools/build_data.py list` to see configured assets and the current local inputs.
- Git ignores `data/rszMHWS.json` and `data/il2cpp_dump.json`. Keep `data/Enums_Internal.json` in Git.
- Re-run `python tools/build_data.py upload` when the matched metadata files change.
- The tool looks for the repository in `GITHUB_REPOSITORY`, `git remote.origin.url`, or `gh repo view`. Use `--repo owner/name` in a folder without a configured remote.
- Use `--tag` to select an alternate release. Download files are kept in `.temp/build_data/` by default. Use `--work-dir` to select a different download directory.
- The Steam patch sources for the small `.user.3` build inputs are listed in the [platform resource notes](../docs/platform-resources.md).
