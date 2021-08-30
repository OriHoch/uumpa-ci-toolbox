import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def docker():
    pass


@docker.command(context_settings={"allow_interspersed_args": False})
@click.option('--cache-from', required=True, help='Docker image to cache from')
@click.argument('DOCKER_BUILD_ARGS', nargs=-1, required=True)
def build_cache(**kwargs):
    """Build a Docker image with optional cache-from argument.

    It first attempts to pull the cache-from image, if it exists - it uses it as cache-from argument,
    otherwise it builds without cache"""
    api.build_cache(**kwargs)
    common.cli_success()


@docker.command()
@click.option('--source-tag-name', required=True)
@click.option('--push-tag-name', required=True)
def tag_push(**kwargs):
    """Tag and push a Docker image.

    It first tags the SOURCE_TAG_NAME with the PUSH_TAG_NAME,
    and then pushes the PUSH_TAG_NAME"""
    api.tag_push(**kwargs)
    common.cli_success()
