"""
FastAPI Backend
"""

import datetime
import logging

from fastapi.responses import FileResponse, HTMLResponse

from ml_server.app.base import MLServerRouter
from ml_server.models import bodies, responses
from ml_server.utils import STATIC_DIR

logger = logging.getLogger(__name__)

utils_router = MLServerRouter(tags=["utilities"])


@utils_router.get("/", include_in_schema=False)
async def index() -> FileResponse:
    """
    Load the Homepage
    """
    return FileResponse(STATIC_DIR.joinpath("index.html"),
                        status_code=200,
                        media_type=HTMLResponse.media_type)


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
async def request(body: bodies.RequestBody) -> bodies.RequestBody:
    """
    Example Post Request with Expected Data
    """
    return body
