"""
Inheritance and Wrapper Classes for MLServer
"""
from typing import Any

from fastapi import APIRouter, FastAPI
from fastapi.templating import Jinja2Templates

from ml_server._version import __ml_server__, __version__
from ml_server.utils import FilePaths

templates = Jinja2Templates(directory=FilePaths.ML_SERVER_DIR.joinpath("templates"))


class MLServerRouter(APIRouter):
    """
    Base API Router Class for MLServer
    """


class MLServer(FastAPI):
    """
    MLServer FastAPI Class
    """

    def __init__(self,
                 debug: bool = True,
                 title: str = __ml_server__,
                 description: str = "Example ML Server with FastAPI",
                 version: str = __version__,
                 **kwargs: Any):
        """
        Initialize A FastAPI Object

        Parameters
        ----------
        debug: bool

        title: str
        description: str
        version: str
        **kwargs
            Arbitrary keyword arguments passed to the FastAPI Object
        """
        super(MLServer, self).__init__(
            debug=debug,
            title=title,
            description=description,
            version=version,
            **kwargs
        )
