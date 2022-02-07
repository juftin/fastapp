"""
ml-server Utilities and Helpers
"""

from pathlib import Path

import yaml


class FilePaths:
    """
    File Path Namespace
    """

    _this_file = Path(__file__).resolve()
    ML_SERVER_DIR = _this_file.parent
    CONFIG_DIR = ML_SERVER_DIR.joinpath("config")
    PROJECT_DIR = ML_SERVER_DIR.parent

    APP_DIR = ML_SERVER_DIR.joinpath("app")
    STATIC_DIR = APP_DIR.joinpath("static")

    GUNICORN_CONFIG_FILE = str(CONFIG_DIR.joinpath("gunicorn_config.py"))
    UVICORN_LOGGING_CONFIG_FILE = str(CONFIG_DIR.joinpath("uvicorn_logging_config.yaml"))
    GUNICORN_LOGGING_CONFIG_FILE = str(CONFIG_DIR.joinpath("gunicorn_logging_config.yaml"))
    NGINX_CONFIG_FILE = str(CONFIG_DIR.joinpath("nginx.conf"))


with open(FilePaths.GUNICORN_LOGGING_CONFIG_FILE, "r") as yaml_file:
    GUNICORN_LOGGING_CONFIG = yaml.load(yaml_file, Loader=yaml.SafeLoader)

UVICORN_LOGGING_CONFIG = GUNICORN_LOGGING_CONFIG.copy()
UVICORN_LOGGING_CONFIG["loggers"] = {}
for logger_name, logger_config in GUNICORN_LOGGING_CONFIG["loggers"].items():
    if "uvicorn" in logger_name:
        UVICORN_LOGGING_CONFIG["loggers"][logger_name] = logger_config
        UVICORN_LOGGING_CONFIG["loggers"][logger_name]["handlers"] = []
