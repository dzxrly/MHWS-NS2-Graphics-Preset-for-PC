from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class EnumLookup:
    def __init__(self, data: dict[str, dict[str, int]]) -> None:
        self._data = data

    @classmethod
    def load(cls, path: Path) -> "EnumLookup":
        with path.open("r", encoding="utf-8") as handle:
            raw = json.load(handle)
        if not isinstance(raw, dict):
            raise ValueError(f"enum file must contain an object: {path}")
        data: dict[str, dict[str, int]] = {}
        for enum_type, members in raw.items():
            if not isinstance(enum_type, str) or not isinstance(members, dict):
                continue
            clean = {
                name: value
                for name, value in members.items()
                if isinstance(name, str) and isinstance(value, int)
            }
            if clean:
                data[enum_type] = clean
        return cls(data)

    def value(self, enum_type: str, member: str) -> int:
        try:
            return self._data[enum_type][member]
        except KeyError as exc:
            raise KeyError(f"enum member not found: {enum_type}.{member}") from exc

    def label(self, enum_type: str, value: int) -> str:
        for member, candidate in self._data[enum_type].items():
            if candidate == value:
                return f"[{value}] {member}"
        raise KeyError(f"enum value not found: {enum_type}={value}")


def enum_int(value: Any) -> int | None:
    """Read raw ints or PyREUser3 labels such as ``[5] PC``."""

    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("[") and "]" in text:
            text = text[1 : text.index("]")]
        try:
            return int(text, 0)
        except ValueError:
            return None
    return None
