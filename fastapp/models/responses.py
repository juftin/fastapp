"""
API Response Objects
"""

import datetime

from fastapp.models import FastAppModel


class PingResponse(FastAppModel):
    """
    Response returned for the `/ping` endpoint
    """

    healthy: bool = True
    status: int
    timestamp: datetime.datetime


class SentimentResponse(FastAppModel):
    """
    Response returned from the `/sentiment` endpoint
    """

    neg: float
    neu: float
    pos: float
    compound: float
