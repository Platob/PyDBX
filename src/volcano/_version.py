"""Volcano package version information."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    """Semantic version container."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.major}.{self.minor}.{self.patch}"


__version_info__ = Version(0, 1, 0)
__version__ = str(__version_info__)

