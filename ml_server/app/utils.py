"""
FastAPI Backend
"""

import logging

from starlette.templating import _TemplateResponse  # noqa

from ml_server.app.base import MLServerRouter
from ml_server.models import bodies

logger = logging.getLogger(__name__)

utils_router = MLServerRouter(tags=["utilities"])


@utils_router.post("/request", response_model=bodies.RequestBody)
async def generic_request(body: bodies.RequestBody) -> bodies.RequestBody:
    """
    Example Post Request with Expected Data
    """
    return body
