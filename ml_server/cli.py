"""
ml-server CLI
"""

import logging
from typing import Optional

import click

from ml_server.serve import start_server, start_server_debug

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)8s]: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@click.group()
@click.pass_context
def cli(ctx: click.core.Context) -> None:
    """
    ml-server: MLOps for Fun
    """
    ctx.ensure_object(dict)


@cli.command()
@click.pass_context
@click.option("--nginx-config", default=None)
def serve(ctx: click.core.Context, nginx_config: Optional[str] = None) -> None:
    """
    Run Nginx and Gunicorn (with the UvicornWorker)
    """
    logger.info("Starting Up Production Server")
    start_server(nginx_config=nginx_config)


@cli.command()
@click.pass_context
def serve_debug(ctx: click.core.Context) -> None:
    """
    Run Uvicorn Debug/Development Server
    """
    logger.info("Starting Up Debug/Development Server")
    start_server_debug()


if __name__ == "__main__":
    cli()
