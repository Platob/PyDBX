"""Top-level package for Volcano.

This starter template provides a production-ready structure inspired by the
`yggdrasil` project while remaining minimal and easy to adapt.
"""

from ._version import __version__
from .core import ignite

__all__ = ["ignite", "__version__"]
