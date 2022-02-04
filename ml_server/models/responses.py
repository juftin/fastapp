"""
API Response Objects
"""

import datetime

from pydantic import BaseModel


class PingResponse(BaseModel):
    """
    Response returned for the `/ping` endpoint
    """

    healthy: bool = True
    status: int
    timestamp: datetime.datetime


class SentimentResponse(BaseModel):
    """
    Response returned from the `/sentiment` endpoint
    """

    neg: float
    neu: float
    pos: float
    compound: float
