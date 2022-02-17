"""
ml-server FastAPI App
"""

from .base import app, MLServer, MLServerRouter

__all__ = [
    "app",
    "MLServer",
    "MLServerRouter",
]
