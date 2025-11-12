"""Command line interface for Volcano."""

from __future__ import annotations

import argparse
from typing import Iterable

from . import ignite
from ._version import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Volcano command line interface")
    parser.add_argument(
        "sources",
        nargs="*",
        help="Event source names to normalize",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"volcano {__version__}",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    normalized = ignite(args.sources)
    for item in normalized:
        print(item)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
