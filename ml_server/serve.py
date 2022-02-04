#!/usr/bin/env python

"""
Uvicorn x Gunicorn x Nginx x FastAPI Configuration
"""

import logging
import multiprocessing
import os
import pathlib
import signal
import subprocess
import sys
from typing import List, Union

import uvicorn

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


def start_server_debug(app: str = "ml_server.app:app",
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
    uvicorn.run(app, host=host, port=port, reload=reload)


def start_server(nginx_config: Union[str, pathlib.Path] = None) -> None:
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
    cpu_count = multiprocessing.cpu_count()
    model_server_timeout = os.environ.get("MODEL_SERVER_TIMEOUT", 60)
    model_server_workers = int(os.environ.get("MODEL_SERVER_WORKERS", cpu_count))

    logger.info("Starting the server with %s workers.", model_server_workers)

    if nginx_config is None:
        nginx_config = pathlib.Path(__file__).resolve().parent.joinpath("config/nginx.conf")
    nginx = subprocess.Popen(["nginx",
                              "-c", str(nginx_config)
                              ])
    gunicorn = subprocess.Popen([
        "gunicorn",
        "--timeout", str(model_server_timeout),
        "--worker-class", "uvicorn.workers.UvicornWorker",
        "--bind", "unix:/tmp/gunicorn.sock",
        "--workers", str(model_server_workers),
        "ml_server.app:app"
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
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)8s]: %(message)s [%(name)s]")
    start_server()
