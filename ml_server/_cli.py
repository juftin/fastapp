"""
ml-server CLI
"""

import logging.config
import sys
from typing import Optional

import click

from ml_server._version import __asgi__, __ml_server__
from ml_server.serve import start_server, start_server_debug

root_logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s [%(levelname)8s] %(name)s: %(message)s")
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
root_logger.setLevel(logging.INFO)
root_logger.addHandler(handler)

logger = logging.getLogger(__name__)

ml_server_app = click.argument("app", default=__asgi__)


@click.group()
@click.version_option(version=click.__version__, prog_name=__ml_server__)
@click.pass_context
def cli(ctx: click.core.Context) -> None:
    """
    ml-server: Command Line Interface
    """
    ctx.ensure_object(dict)


@cli.command()
@ml_server_app
@click.pass_context
@click.option("--nginx-config", default=None,
              help="Path to Custom Nginx Configuration File")
def serve(ctx: click.core.Context, app: str,
          nginx_config: Optional[str] = None) -> click.core.Context:
    """
    Run Nginx and Gunicorn (with the UvicornWorker)

    Pass the python path of the
    app to run. Defaults to `ml_server:app`
    """
    start_server(asgi_app=app, nginx_config=nginx_config)
    return ctx


@cli.command()
@ml_server_app
@click.pass_context
def serve_debug(ctx: click.core.Context, app: str) -> click.core.Context:
    """
    Run Uvicorn Debug/Development Server.

    Pass the python path of the
    app to run. Defaults to `ml_server:app`
    """
    start_server_debug(app=app)
    return ctx


if __name__ == "__main__":
    cli()