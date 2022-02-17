"""
Inheritance and Wrapper Classes for FastApp
"""

import datetime
from typing import Any

from fastapi import APIRouter, FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse  # noqa

from fastapp._utils import FilePaths
from fastapp._version import __fastapp__, __version__
from fastapp.models.responses import PingResponse


class FastAppRouter(APIRouter):
    """
    Base API Router Class for FastApp
    """


class FastApp(FastAPI):
    """
    FastApp FastAPI Class
    """

    def __init__(self,
                 debug: bool = True,
                 title: str = __fastapp__,
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
        super(FastApp, self).__init__(
            debug=debug,
            title=title,
            description=description,
            version=version,
            **kwargs
        )


app = FastApp()


def mount_static_app(fastapp_app: FastApp) -> FastApp:
    """
    Mount the fastapp internal static directory to an app

    Parameters
    ----------
    fastapp_app: FastApp
        App to mount directory onto

    Returns
    -------
    FastApp
    """
    _static_dir = FilePaths.APP_DIR.joinpath("static")
    fastapp_app.mount("/static", StaticFiles(directory=_static_dir), name="static")
    return fastapp_app


mount_static_app(app)
templates = Jinja2Templates(directory=FilePaths.APP_DIR.joinpath("templates"))
fastapp_router = FastAppRouter(tags=["fastapp"])


@fastapp_router.get("/", include_in_schema=False, response_class=HTMLResponse)
async def index(request: Request) -> _TemplateResponse:
    """
    Load the Homepage
    """
    return templates.TemplateResponse(name="index.html",
                                      context=dict(request=request, version=__version__)
                                      )


@fastapp_router.get("/ping", response_model=PingResponse)
async def ping() -> PingResponse:
    """
    Return a Health Response
    """
    return PingResponse(healthy=True,
                        status=200,
                        timestamp=datetime.datetime.utcnow())


app.include_router(router=fastapp_router)
