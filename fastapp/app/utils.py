"""
FastAPI Backend
"""

import logging

from starlette.templating import _TemplateResponse  # noqa

from fastapp.app.base import FastAppRouter
from fastapp.models import bodies

logger = logging.getLogger(__name__)

utils_router = FastAppRouter(tags=["utilities"])


@utils_router.post("/request", response_model=bodies.RequestBody)
async def generic_request(body: bodies.RequestBody) -> bodies.RequestBody:
    """
    Example Post Request with Expected Data
    """
    return body
