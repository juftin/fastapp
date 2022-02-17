"""
FastApp Example FastAPI App

pip install fastapp[example]
"""

import json

from fastapi.templating import Jinja2Templates

from fastapp.app.base import fastapp_router, FastApp, FastAppRouter, mount_static_app
from fastapp.app.machine_learning import machine_learning_router
from fastapp.app.utils import utils_router
from fastapp._utils import FilePaths

app = FastApp()

mount_static_app(app)
templates = Jinja2Templates(directory=FilePaths.APP_DIR.joinpath("templates"))

router: FastAppRouter
for router in [
    fastapp_router,
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
