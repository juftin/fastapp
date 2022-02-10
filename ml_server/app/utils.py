"""
FastAPI Backend
"""

import datetime
import logging

from fastapi import Request
from fastapi.responses import HTMLResponse

from ml_server._version import __version__
from ml_server.app.base import MLServerRouter, templates
from ml_server.models import bodies, responses

logger = logging.getLogger(__name__)

utils_router = MLServerRouter(tags=["utilities"])


@utils_router.get("/", include_in_schema=False, response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """
    Load the Homepage
    """
    return templates.TemplateResponse(name="index.html",
                                      context=dict(request=request, version=__version__)
                                      )


@utils_router.get("/ping", response_model=responses.PingResponse)
async def ping() -> responses.PingResponse:
    """
    Return a Health Response
    """
    health = True
    status = 200 if health is True else 404
    return responses.PingResponse(healthy=health,
                                  status=status,
                                  timestamp=datetime.datetime.utcnow())


@utils_router.post("/request", response_model=bodies.RequestBody)
async def generic_request(body: bodies.RequestBody) -> bodies.RequestBody:
    """
    Example Post Request with Expected Data
    """
    return body
