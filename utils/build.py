from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory

from pyreuser3 import REUser3Converter

from . import (
    APP_STREAMING,
    GRASS_CULLING,
    GRAPHICS_PLATFORM,
    GRAPHICS_PRESET,
    GRAPHICS_USAGE,
    OPTION_GRAPHICS,
    OPTION_PRESET,
    VARIANTS,
)
from .build_log import OutputLog
from .enums import EnumLookup
from .package import read_version, write_mod_archive, write_modinfo
from .patches import (
    graphics_profile,
    patch_app_streaming,
    patch_graphics_preset,
    patch_grass_culling,
    patch_option_graphics,
    patch_option_presets,
)
from .verify import verify_option_identities, verify_rebuilt


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build MHWS NS2 Graphics Preset for PC."
    )
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument(
        "--metadata-dir",
        type=Path,
        help="Directory with RSZ and IL2CPP JSON (default: data directory)",
    )
    parser.add_argument("--assets-dir", type=Path, default=Path("assets"))
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    parser.add_argument("--version-file", type=Path, default=Path("version.json"))
    parser.add_argument("--variant", choices=("all", *VARIANTS), default="all")
    args = parser.parse_args(args=argv)

    root = Path(__file__).resolve().parents[1]
    data_dir = root / args.data_dir
    assets_dir = root / args.assets_dir
    metadata_dir = root / args.metadata_dir if args.metadata_dir else data_dir
    output_dir = root / args.output_dir
    version = read_version(path=root / args.version_file)
    enums = EnumLookup.load(path=data_dir / "Enums_Internal.json")
    variants = VARIANTS if args.variant == "all" else (args.variant,)
    schema = metadata_dir / "rszMHWS.json"
    il2cpp = metadata_dir / "il2cpp_dump.json"
    for path in (
        schema,
        il2cpp,
        data_dir / GRAPHICS_PRESET,
        data_dir / OPTION_PRESET,
        data_dir / OPTION_GRAPHICS,
        data_dir / GRASS_CULLING,
        data_dir / APP_STREAMING,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)

    output_dir.mkdir(parents=True, exist_ok=True)
    with (
        OutputLog(path=output_dir / "output.log") as log,
        TemporaryDirectory(dir=output_dir, prefix="_package_") as staging_dir,
    ):
        stage = Path(staging_dir)
        converter = REUser3Converter(
            schema_path=schema,
            il2cpp_dump_path=il2cpp,
        )
        log.section(title=f"Build {version}")
        log.line(text=f"Game metadata: {metadata_dir}")
        log.line(text=f"Source resources: {data_dir}")

        print("Reading graphics build inputs...")
        graphics = converter.parse_pack_file(user3_path=data_dir / GRAPHICS_PRESET)
        options = converter.parse_pack_file(user3_path=data_dir / OPTION_PRESET)
        option_graphics = converter.parse_pack_file(
            user3_path=data_dir / OPTION_GRAPHICS
        )
        grass = converter.parse_pack_file(user3_path=data_dir / GRASS_CULLING)
        streaming = converter.parse_pack_file(user3_path=data_dir / APP_STREAMING)
        changes = patch_app_streaming(data=streaming, enums=enums)
        log.section(title=APP_STREAMING.name)
        log.lines(values=changes)

        package_dir = stage / "mod"
        streaming_path = package_dir / APP_STREAMING
        streaming_path.parent.mkdir(parents=True, exist_ok=True)
        streaming_path.write_bytes(converter.pack(data=streaming))
        verify_rebuilt(
            expected=streaming,
            rebuilt=converter.parse_pack_file(user3_path=streaming_path),
        )
        log.line(
            text="Verification passed: rebuilt USER/RSZ document matches the edited source."
        )

        usage = enums.value(enum_type=GRAPHICS_USAGE, member="Default")
        archives = []
        for variant in variants:
            platform = enums.value(
                enum_type=GRAPHICS_PLATFORM, member=VARIANTS[variant]
            )
            variant_graphics = deepcopy(graphics)
            variant_options = deepcopy(options)
            variant_option_graphics = deepcopy(option_graphics)
            variant_grass = deepcopy(grass)
            profile = graphics_profile(
                data=variant_graphics, platform=platform, usage=usage
            )
            pc_usages = patch_graphics_preset(
                data=variant_graphics, profile=profile, enums=enums
            )
            menu_options = patch_option_graphics(
                data=variant_option_graphics,
                graphics=variant_graphics,
                profile=profile,
                enums=enums,
            )
            patch_option_presets(
                data=variant_options,
                profile=profile,
                menu_options=menu_options,
            )
            grass_rows = patch_grass_culling(
                data=variant_grass, profile=profile, enums=enums
            )
            log.section(title=variant.title())
            log.line(text=f"GraphicsPreset source key: {VARIANTS[variant]}/{usage}")
            log.line(
                text=f"Synchronized all {len(pc_usages)} PC GraphicsPreset usages: {sorted(pc_usages)}"
            )
            log.line(
                text="Synchronized all five PC menu tiers, including Balanced upscaling, Standard texture, terrain and culling."
            )
            log.line(
                text=f"Synchronized render payloads for {len(menu_options)} OptionGraphicsData groups."
            )
            log.line(
                text=f"Synchronized grass density in {grass_rows} {profile['_GrassCullingMode']} rows."
            )
            for member, data in (
                (GRAPHICS_PRESET, variant_graphics),
                (OPTION_PRESET, variant_options),
                (OPTION_GRAPHICS, variant_option_graphics),
                (GRASS_CULLING, variant_grass),
            ):
                target = package_dir / member
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(converter.pack(data=data))
                rebuilt = converter.parse_pack_file(user3_path=target)
                verify_rebuilt(expected=data, rebuilt=rebuilt)
                if member == OPTION_GRAPHICS:
                    verify_option_identities(original=option_graphics, rebuilt=rebuilt)
                    log.line(
                        text="Verified all original OptionGraphicsData _Option identities."
                    )
                log.line(text=f"Verification passed: {member.name}")
            modinfo = write_modinfo(
                package_dir=package_dir,
                assets_dir=assets_dir,
                variant=variant,
                version=version,
            )
            archive = write_mod_archive(
                package_dir=package_dir,
                output_dir=stage,
                members=(
                    GRAPHICS_PRESET,
                    OPTION_PRESET,
                    OPTION_GRAPHICS,
                    GRASS_CULLING,
                    APP_STREAMING,
                    modinfo,
                ),
                variant=variant,
                version=version,
            )
            archives.append(archive)

        for archive in archives:
            final = archive.replace(output_dir / archive.name)
            log.line(text=f"Built: {final}")
            print(final)
    return 0
