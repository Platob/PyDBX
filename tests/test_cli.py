"""CLI tests for Volcano."""

from __future__ import annotations

from volcano import cli


def test_cli_lists_normalized_sources(capsys):
    exit_code = cli.main(["Lava", "Ash"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip().splitlines() == ["ash", "lava"]
