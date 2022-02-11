"""
API Request Body Containers
"""

from typing import List, Union

from ml_server.models import MLServerModel


class RequestBody(MLServerModel):
    """
    Data body for the generic `/request` endpoint
    """

    example: int
    another_example: str


class GensimRequest(MLServerModel):
    """
    Data body for requests to the `/most_similar` endpoint
    """

    positive: List[str] = []
    negative: List[str] = []
    topn: int = 10


class SentimentRequest(MLServerModel):
    """
    Request Format for the `/sentiment` endpoint
    """

    text: Union[str, List[str]]
