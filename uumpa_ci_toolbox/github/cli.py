import json

import click

from .actions.cli import actions
from . import api


@click.group()
def github():
    pass


github.add_command(actions)


@github.command()
@click.argument('REPOSITORY')
@click.argument('KEY_TITLE')
@click.argument('PUBLIC_KEY')
@click.option('--read-only')
def create_deploy_key(**kwargs):
    print(json.dumps(api.create_deploy_key(**kwargs)))
    print('OK')


@github.command()
@click.argument('REPOSITORY')
@click.argument('KEY')
@click.argument('VALUE')
def add_environment_secret(**kwargs):
    api.add_environment_secret(**kwargs)
    print('OK')


@github.command()
@click.argument('CREATE_DEPLOY_KEY_REPOSITORY')
@click.argument('ADD_ENVIRONMENT_SECRET_REPOSITORY')
@click.argument('DEPLOY_KEY_TITLE')
@click.argument('ENVIRONMENT_SECRET_NAME')
def create_and_configure_deploy_key(**kwargs):
    api.create_and_configure_deploy_key(**kwargs)
    print('OK')