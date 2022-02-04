"""
ml-server FastAPI App
"""

import json
from pathlib import Path

from fastapi import FastAPI

from ml_server import __ml_server__, __version__
from ml_server.app.machine_learning import machine_learning_router
from ml_server.app.utils import utils_router

app = FastAPI(debug=True,
              title=__ml_server__,
              description="Example ML Server with FastAPI",
              version=__version__)

for router in [
    machine_learning_router,
    utils_router,
]:
    app.include_router(router=router)

if __name__ == "__main__":
    _package_dir = Path(__file__).resolve().parent.parent
    json_file_path = _package_dir.joinpath("config").joinpath("swagger.json")
    openapi_spec = app.openapi()
    openapi_spec["servers"] = [
        dict(url="http://localhost:8080/")
    ]

    with open(json_file_path, "w") as json_file:
        json.dump(openapi_spec, json_file, indent=4)
