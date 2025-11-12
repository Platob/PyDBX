"""Test configuration for Volcano."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the src directory is available on sys.path for local testing without installation.
SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
if SRC_ROOT.exists():
    sys.path.insert(0, str(SRC_ROOT))
