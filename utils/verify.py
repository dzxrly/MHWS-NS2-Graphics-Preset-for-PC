from __future__ import annotations

from .repack import JsonDict, instances


def verify_rebuilt(expected: JsonDict, rebuilt: JsonDict) -> None:
    # _source.file records the path used by the parser and is external to the binary.
    expected["_source"].pop("file", None)
    rebuilt["_source"].pop("file", None)
    if expected != rebuilt:
        keys = [
            key
            for key in expected.keys() | rebuilt.keys()
            if expected.get(key) != rebuilt.get(key)
        ]
        raise ValueError(
            f"repacked USER/RSZ document differs in: {', '.join(sorted(keys))}"
        )


def verify_option_identities(original: JsonDict, rebuilt: JsonDict) -> None:
    identities = []
    for data in (original, rebuilt):
        identities.append(
            {
                index: entry["fields"]["_Option"]
                for index, entry in instances(data=data).items()
                if "_Option" in entry.get("fields", {})
            },
        )
    if identities[0] != identities[1]:
        raise ValueError("OptionGraphicsData _Option identities changed")
