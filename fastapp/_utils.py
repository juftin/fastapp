"""
FastApp Utilities and Helpers
"""

from pathlib import Path

import yaml


class FilePaths:
    """
    File Path Namespace
    """

    _this_file = Path(__file__).resolve()
    FASTAPP_DIR = _this_file.parent
    CONFIG_DIR = FASTAPP_DIR.joinpath("config")
    PROJECT_DIR = FASTAPP_DIR.parent

    APP_DIR = FASTAPP_DIR.joinpath("app")
    STATIC_DIR = APP_DIR.joinpath("static")

    GUNICORN_CONFIG_FILE = str(CONFIG_DIR.joinpath("gunicorn_config.py"))
    GUNICORN_LOGGING_CONFIG_FILE = str(CONFIG_DIR.joinpath("logging_config.yaml"))
    UVICORN_LOGGING_CONFIG_FILE = str(CONFIG_DIR.joinpath("uvicorn_logging_config.yaml"))
    NGINX_CONFIG_FILE = str(CONFIG_DIR.joinpath("nginx.conf"))


with open(FilePaths.GUNICORN_LOGGING_CONFIG_FILE, "r") as yaml_file:
    GUNICORN_LOGGING_CONFIG = yaml.load(yaml_file, Loader=yaml.SafeLoader)
