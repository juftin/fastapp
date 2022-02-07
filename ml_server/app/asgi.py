"""
ml-server FastAPI App
"""

import json

from fastapi.staticfiles import StaticFiles

from ml_server.app.base import MLServer, MLServerRouter
from ml_server.app.machine_learning import machine_learning_router
from ml_server.app.utils import utils_router
from ml_server.utils import FilePaths

app = MLServer()
_static_dir = FilePaths.APP_DIR.joinpath("static")
app.mount("/static", StaticFiles(directory=_static_dir), name="static")

router: MLServerRouter
for router in [
    machine_learning_router,
    utils_router,
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
