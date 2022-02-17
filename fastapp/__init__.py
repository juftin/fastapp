"""
fastapp
"""

from ._version import __version__
from .app import app, FastApp, FastAppRouter
from .models import FastAppModel

__all__ = [
    "__version__",
    "FastApp",
    "FastAppRouter",
    "FastAppModel",
    "app",
]
