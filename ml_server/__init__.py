"""
ml-server
"""

from ._version import __version__
from .app import app, MLServer, MLServerRouter
from .models import MLServerModel

__all__ = [
    "__version__",
    "MLServer",
    "MLServerRouter",
    "MLServerModel",
    "app",
]
