"""
ml-server Example FastAPI App

pip install ml-server[example]
"""

import json

from fastapi.templating import Jinja2Templates

from ml_server.app.base import ml_server_router, MLServer, MLServerRouter, mount_static_app
from ml_server.app.machine_learning import machine_learning_router
from ml_server.app.utils import utils_router
from ml_server._utils import FilePaths

app = MLServer()

mount_static_app(app)
templates = Jinja2Templates(directory=FilePaths.APP_DIR.joinpath("templates"))

router: MLServerRouter
for router in [
    ml_server_router,
    utils_router,
    machine_learning_router,
]:
    app.include_router(router=router)

if __name__ == "__main__":
    json_file_path = FilePaths.CONFIG_DIR.joinpath("swagger.json")
    openapi_spec = app.openapi()
    openapi_spec["servers"] = [
        dict(url="http://localhost:8080/")
    ]

    with open(json_file_path, "w") as json_file:
        json.dump(openapi_spec, json_file, indent=4)
