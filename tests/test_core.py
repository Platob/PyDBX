"""Tests for the Volcano core utilities."""

from __future__ import annotations

import pytest

from volcano.core import ignite


def test_ignite_normalizes_and_sorts_sources():
    sources = [" Lava ", "ash", "lava", "SMOKE"]
    assert ignite(sources) == ["ash", "lava", "smoke"]


def test_ignite_handles_empty_values():
    sources = ["", "   ", "steam"]
    assert ignite(sources) == ["steam"]


@pytest.mark.parametrize("sources", [[""], []])
def test_ignite_returns_empty_list_when_no_valid_sources(sources):
    assert ignite(sources) == []
