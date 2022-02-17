ARG BASE_IMAGE="python:3.9.10"
FROM ${BASE_IMAGE}

MAINTAINER juftin@juftin.com

SHELL ["/bin/bash", "-c"]

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
         sudo \
         wget \
         nginx \
         ca-certificates \
         git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip wheel setuptools cython

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
RUN python -m nltk.downloader word2vec_sample vader_lexicon

COPY . /root/fastapp
ENV PYTHONPATH="/root/fastapp:${PYTHONPATH}"

#COPY . /tmp/fastapp
#RUN pip install /tmp/fastapp && rm -rf /tmp/fastapp
#RUN python -m nltk.downloader popular

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

ENV HOME="/root"
RUN mkdir ${HOME}/fastapp
WORKDIR  ${HOME}/fastapp

ENTRYPOINT ["python", "/root/fastapp/fastapp/__main__.py"]

CMD ["--help"]
