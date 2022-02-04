"""
FastAPI Backend
"""

import datetime
import json
import logging
from pathlib import Path
from typing import List, Union

from fastapi import FastAPI
import gensim
from nltk import download
from nltk.data import find
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from ml_server.models import bodies, responses

logger = logging.getLogger(__name__)

for (dataset_name, nltk_dataset) in [
    ("models/word2vec_sample/pruned.word2vec.txt", "word2vec_sample"),
    ("sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt", "vader_lexicon")
]:
    try:
        find(dataset_name)
    except LookupError:
        download(nltk_dataset)

word2vec_sample = str(find("models/word2vec_sample/pruned.word2vec.txt"))
gensim_model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)

sid = SentimentIntensityAnalyzer()

app = FastAPI(debug=True,
              title="ml-server",
              description="Example ML Server with FastAPI",
              version="0.1.0")


@app.get("/ping", response_model=responses.PingResponse)
async def ping() -> responses.PingResponse:
    """
    Return a Health Response
    """
    health = True
    status = 200 if health else 404
    return responses.PingResponse(healthy=health,
                                  status=status,
                                  timestamp=datetime.datetime.utcnow())


@app.post("/request", response_model=bodies.RequestBody)
async def request(body: bodies.RequestBody) -> bodies.RequestBody:
    """
    Example Post Request with Expected Data
    """
    return body


@app.post("/most_similar")
def get_most_similar(body: bodies.GensimRequest) -> List[List[Union[str, float]]]:
    """
    Get a Gensim `gensim.most_similar` response
    """
    return gensim_model.most_similar(positive=body.positive,
                                     negative=body.negative,
                                     topn=body.topn)


@app.post("/sentiment", response_model=List[responses.SentimentResponse])
def get_sentiment(text: bodies.SentimentRequest) -> List[responses.SentimentResponse]:
    """
    Get a `SentimentIntensityAnalyzer` polarity_scores response
    """
    results = []
    if isinstance(text.text, list):
        for text_blob in text.text:
            ss = sid.polarity_scores(text_blob)
            results.append(ss)
    else:
        ss = sid.polarity_scores(text=text.text)
        results.append(dict(ss))
    return results


if __name__ == "__main__":
    json_file_path = Path(__file__).resolve().parent.joinpath("config").joinpath("openapi.json")
    openapi_spec = app.openapi()
    with open(json_file_path, "w") as json_file:
        json.dump(openapi_spec, json_file, indent=4)
