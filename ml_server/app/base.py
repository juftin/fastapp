"""
Inheritance and Wrapper Classes for MLServer
"""

import datetime
from typing import Any

from fastapi import APIRouter, FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse  # noqa

from ml_server._utils import FilePaths
from ml_server._version import __ml_server__, __version__
from ml_server.models.responses import PingResponse


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


app = MLServer()


def mount_static_app(mlserver_app: MLServer) -> MLServer:
    """
    Mount the ml-server internal static directory to an app

    Parameters
    ----------
    mlserver_app: MLServer
        App to mount directory onto

    Returns
    -------
    MLServer
    """
    _static_dir = FilePaths.APP_DIR.joinpath("static")
    mlserver_app.mount("/static", StaticFiles(directory=_static_dir), name="static")
    return mlserver_app


mount_static_app(app)
templates = Jinja2Templates(directory=FilePaths.APP_DIR.joinpath("templates"))
ml_server_router = MLServerRouter(tags=["ml-server"])


@ml_server_router.get("/", include_in_schema=False, response_class=HTMLResponse)
async def index(request: Request) -> _TemplateResponse:
    """
    Load the Homepage
    """
    return templates.TemplateResponse(name="index.html",
                                      context=dict(request=request, version=__version__)
                                      )


@ml_server_router.get("/ping", response_model=PingResponse)
async def ping() -> PingResponse:
    """
    Return a Health Response
    """
    return PingResponse(healthy=True,
                        status=200,
                        timestamp=datetime.datetime.utcnow())


app.include_router(router=ml_server_router)
