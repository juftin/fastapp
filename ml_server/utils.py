"""
ml-server Utilities and Helpers
"""
from pathlib import Path

import yaml

_this_file = Path(__file__).resolve()

ML_SERVER_DIR = _this_file.parent
CONFIG_DIR = ML_SERVER_DIR.joinpath("config")
PROJECT_DIR = ML_SERVER_DIR.parent

APP_DIR = ML_SERVER_DIR.joinpath("app")
STATIC_DIR = APP_DIR.joinpath("static")

LOGGING_CONFIG_FILE = str(CONFIG_DIR.joinpath("logging_config.yaml"))
GUNICORN_CONFIG_FILE = str(CONFIG_DIR.joinpath("gunicorn_config.py"))
NGINX_CONFIG_FILE = str(CONFIG_DIR.joinpath("nginx.conf"))

with open(LOGGING_CONFIG_FILE, "r") as yaml_file:
    LOGGING_CONFIG = yaml.load(yaml_file, Loader=yaml.SafeLoader)
