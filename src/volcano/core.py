"""Core utilities for the Volcano package."""

from __future__ import annotations

from typing import Iterable, List


def ignite(sources: Iterable[str]) -> List[str]:
    """Return a normalized list of unique event source identifiers.

    The helper demonstrates a simple business rule with traceable behaviour and
    serves as a starting point for real functionality.
    """

    unique_sources = {source.strip().lower() for source in sources if source.strip()}
    return sorted(unique_sources)


__all__ = ["ignite"]
