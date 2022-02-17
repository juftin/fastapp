"""
FastAPI Backend
"""

import logging
from typing import List, Union

import gensim
from nltk import download
from nltk.data import find
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from fastapp.app.base import FastAppRouter
from fastapp.models import bodies, responses

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

machine_learning_router = FastAppRouter(prefix="/ml",
                                        tags=["machine learning"])


@machine_learning_router.post("/most_similar")
def get_most_similar(body: bodies.GensimRequest) -> List[List[Union[str, float]]]:
    """
    Get a Gensim `gensim.most_similar` response
    """
    return gensim_model.most_similar(positive=body.positive,
                                     negative=body.negative,
                                     topn=body.topn)


@machine_learning_router.post("/sentiment", response_model=List[responses.SentimentResponse])
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
