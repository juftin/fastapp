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

ml_server_reference = click.option(
    "--asgi-app", default=__asgi__,
    help="ASGI App Path - Defaults to MLServer Built-In (ml_server.app.app)")


@click.group()
@click.version_option(version=click.__version__, prog_name=__ml_server__)
@click.pass_context
def cli(ctx: click.core.Context) -> None:
    """
    ml-server: Command Line Interface
    """
    ctx.ensure_object(dict)


@cli.command()
@click.pass_context
@click.option("--nginx-config", default=None,
              help="Nginx Configuration File - Defaults to MLServer Built-In")
@ml_server_reference
def serve(ctx: click.core.Context, nginx_config: Optional[str] = None,
          asgi_app: str = __asgi__) -> click.core.Context:
    """
    Run Nginx and Gunicorn (with the UvicornWorker)
    """
    start_server(asgi_app=asgi_app, nginx_config=nginx_config)
    return ctx


@cli.command()
@click.pass_context
@ml_server_reference
def serve_debug(ctx: click.core.Context,
                asgi_app: str = __asgi__) -> click.core.Context:
    """
    Run Uvicorn Debug/Development Server
    """
    start_server_debug(app=asgi_app)
    return ctx


if __name__ == "__main__":
    cli()
