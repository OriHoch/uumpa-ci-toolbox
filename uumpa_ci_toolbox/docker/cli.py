import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def docker():
    pass


@docker.command(context_settings={"allow_interspersed_args": False})
@click.option('--cache-from')
@click.argument('DOCKER_BUILD_ARGS', nargs=-1)
def build_cache(**kwargs):
    api.build_cache(**kwargs)


@docker.command()
@click.argument('SOURCE_TAG_NAME')
@click.argument('PUSH_TAG_NAME')
def tag_push(**kwargs):
    api.tag_push(**kwargs)
