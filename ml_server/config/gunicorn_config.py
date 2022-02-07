"""
Gunicorn Configuration File
"""

import multiprocessing
import os

from ml_server.utils import LOGGING_CONFIG

cpu_count = multiprocessing.cpu_count()

workers = int(os.environ.get("GUNICORN_WORKERS", cpu_count))
timeout = int(os.environ.get("GUNICORN_TIMEOUT", 30))
bind = os.environ.get("GUNICORN_BIND", "unix:/tmp/gunicorn.sock")

worker_class = os.environ.get("GUNCORN_WORKER_CLASS", "uvicorn.workers.UvicornWorker")

logconfig_dict = LOGGING_CONFIG
syslog = True
