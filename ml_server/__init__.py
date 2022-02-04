"""
ml-server
"""

from ._version import __ml_server__, __version__
from .serve import start_server

__all__ = [
    "start_server",
    "__ml_server__",
    "__version__",
]
