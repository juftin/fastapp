"""
API Response Objects
"""

import datetime

from ml_server.models import MLServerModel


class PingResponse(MLServerModel):
    """
    Response returned for the `/ping` endpoint
    """

    healthy: bool = True
    status: int
    timestamp: datetime.datetime


class SentimentResponse(MLServerModel):
    """
    Response returned from the `/sentiment` endpoint
    """

    neg: float
    neu: float
    pos: float
    compound: float
