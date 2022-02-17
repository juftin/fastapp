"""
API Request Body Containers
"""

from typing import List, Union

from fastapp.models import FastAppModel


class RequestBody(FastAppModel):
    """
    Data body for the generic `/request` endpoint
    """

    example: int
    another_example: str


class GensimRequest(FastAppModel):
    """
    Data body for requests to the `/most_similar` endpoint
    """

    positive: List[str] = []
    negative: List[str] = []
    topn: int = 10


class SentimentRequest(FastAppModel):
    """
    Request Format for the `/sentiment` endpoint
    """

    text: Union[str, List[str]]
