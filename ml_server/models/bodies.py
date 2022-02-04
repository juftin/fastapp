"""
API Request Body Containers
"""

from typing import List, Union

from pydantic import BaseModel


class RequestBody(BaseModel):
    """
    Data body for the generic `/request` endpoint
    """

    example: int
    another_example: str


class GensimRequest(BaseModel):
    """
    Data body for requests to the `/most_similar` endpoint
    """

    positive: List[str] = []
    negative: List[str] = []
    topn: int = 10


class SentimentRequest(BaseModel):
    """
    Request Format for the `/sentiment` endpoint
    """

    text: Union[str, List[str]]
