from __future__ import annotations

import json
from pathlib import Path
from string import Template
from zipfile import ZIP_DEFLATED, ZipFile


def read_version(path: Path) -> str:
    version = json.loads(s=path.read_text(encoding="utf-8"))["version"]
    if (
        not isinstance(version, str)
        or not version
        or not version.replace(".", "").isalnum()
    ):
        raise ValueError(f"invalid archive version in {path}")
    return version


def write_modinfo(
    package_dir: Path,
    assets_dir: Path,
    variant: str,
    version: str,
) -> Path:
    modinfo = Path("modinfo.ini")
    (package_dir / modinfo).write_text(
        Template((assets_dir / modinfo).read_text(encoding="utf-8")).substitute(
            mode=variant.title(),
            version=version,
        ),
        encoding="utf-8",
        newline="\n",
    )
    return modinfo


def write_mod_archive(
    package_dir: Path,
    output_dir: Path,
    members: tuple[Path, ...],
    variant: str,
    version: str,
) -> Path:
    archive_path = (
        output_dir / f"MHWS_NS2_Graphics_Preset_for_PC_{variant.title()}_{version}.zip"
    )
    with ZipFile(file=archive_path, mode="w", compression=ZIP_DEFLATED) as archive:
        for member in members:
            archive.write(filename=package_dir / member, arcname=member.as_posix())
    with ZipFile(file=archive_path) as archive:
        damaged_member = archive.testzip()
        if damaged_member is not None:
            raise ValueError(f"{archive_path}: damaged member {damaged_member}")
    return archive_path
