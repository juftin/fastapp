#!/usr/bin/env python

"""
Uvicorn x Gunicorn x Nginx x FastAPI Configuration
"""

import logging
import os
import pathlib
import signal
import subprocess
import sys
from typing import List, Union

import uvicorn

from ml_server._utils import (FilePaths,
                              UVICORN_LOGGING_CONFIG)
from ml_server._version import __asgi__
from ml_server.config import gunicorn_config

logger = logging.getLogger(__name__)


def sigterm_handler(pids: List[int]) -> None:
    """
    Termination Signal Handler

    Parameters
    ----------
    pids: List[int]
        List of Process PIDs

    Returns
    -------
    None
    """
    for process_pid in pids:
        try:
            os.kill(process_pid, signal.SIGQUIT)
        except OSError:
            pass
    sys.exit(0)


def start_server_debug(app: str,
                       host: str = "0.0.0.0",
                       port: int = 8080,
                       reload: bool = True) -> None:
    """
    Start the Uvicorn Development Server

    This server also has live loading

    Parameters
    ----------
    app: str
        FastAPI Object Reference
    host: str
        API Host, defaults to "0.0.0.0"
    port: int
        API Port
    reload: bool
        Whether to Reload the API Source in real-time. This consumes more
        resources.

    Returns
    -------
    None
    """
    logger.info(f"Starting Up Debug/Development Server: {app}")
    uvicorn.run(app,
                host=host,
                port=port,
                reload=reload,
                log_config=UVICORN_LOGGING_CONFIG
                )


def start_server(asgi_app: str, nginx_config: Union[str, pathlib.Path] = None) -> None:
    """
    Start the Nginx and Gunicorn Proceses

    The Gunicorn process uses the uvicorn.workers.UvicornWorker worker
    and binds itself to the Gunicorn .sock which is picked up by Nginx.
    The result is a capable server meant to run on a single instance.

    If you wanted to scale this to a solution like Kubernetes you would
    handle replication at the cluster lecel instead of Gunicorn doing it for
    you. More info at https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

    Returns
    -------
    None
    """
    logger.info("Starting Up Production Server: %s", asgi_app)
    logger.info("Starting the server with %s workers.", gunicorn_config.workers)

    if nginx_config is None:
        nginx_config = FilePaths.NGINX_CONFIG_FILE
    nginx = subprocess.Popen(["nginx",
                              "-c", nginx_config
                              ])
    gunicorn = subprocess.Popen([
        "gunicorn",
        "--config", FilePaths.GUNICORN_CONFIG_FILE,
        asgi_app
    ])
    signal.signal(signal.SIGTERM, lambda a, b: sigterm_handler([nginx.pid, gunicorn.pid]))
    process_pids = {nginx.pid, gunicorn.pid}
    while True:
        pid, _ = os.wait()
        if pid in process_pids:
            break
    sigterm_handler(pids=[nginx.pid, gunicorn.pid])
    logger.info("Server exiting")


if __name__ == "__main__":
    start_server(asgi_app=__asgi__)
