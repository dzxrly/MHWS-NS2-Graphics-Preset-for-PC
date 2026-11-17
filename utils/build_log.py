from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import TextIO


class OutputLog:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._handle: TextIO | None = None

    def __enter__(self) -> "OutputLog":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._handle = self.path.open("w", encoding="utf-8", newline="\n")
        self.line(text="MHWS NS2 Graphics Preset for PC build log")
        self.line(f"Started: {datetime.now().isoformat(timespec='seconds')}")
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        if exc is None:
            self.line(f"Finished: {datetime.now().isoformat(timespec='seconds')}")
        else:
            self.line(f"Failed: {datetime.now().isoformat(timespec='seconds')}")
            self.line(f"Error: {exc!r}")
        if self._handle is not None:
            self._handle.close()

    def section(self, title: str) -> None:
        self.line("")
        self.line("=" * 80)
        self.line(title)
        self.line("=" * 80)

    def line(self, text: str = "") -> None:
        if self._handle is None:
            raise RuntimeError("output log is not open")
        self._handle.write(f"{text}\n")
        self._handle.flush()

    def lines(self, values: list[str]) -> None:
        for value in values:
            self.line(value)
