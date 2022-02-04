"""
FastAPI Backend
"""

import datetime
import logging

from fastapi import APIRouter

from ml_server.models import bodies, responses

logger = logging.getLogger(__name__)

utils_router = APIRouter(tags=["utilities"])


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
