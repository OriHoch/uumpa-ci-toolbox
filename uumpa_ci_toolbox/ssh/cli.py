import click

from . import api


@click.group()
def ssh():
    pass


@ssh.command()
@click.argument('COMMENT')
@click.argument('FILENAME')
def key_gen(**kwargs):
    api.key_gen(**kwargs)
