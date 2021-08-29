import click

from .actions.cli import actions


@click.group()
def github():
    pass


github.add_command(actions)
