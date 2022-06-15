import json

import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def vault():
    pass


@vault.command()
@click.option('--version', required=True, help='Vault version to install, e.g. "1.10.4"')
@click.option('--target-filename', default='/usr/local/bin/vault')
@click.option('--with-sudo', is_flag=True)
def install(**kwargs):
    """Install Vault in the given version"""
    api.install(**kwargs)
    common.cli_success()


@vault.command()
@click.option('--role', required=True)
@click.option('--policy', required=True)
def create_approle(**kwargs):
    """Create an approle to be used in automation"""
    print(json.dumps(api.create_approle(**kwargs)))
    common.cli_success()


@vault.command()
@click.argument('ROLE_ID')
@click.argument('SECRET_ID')
def approle_login(**kwargs):
    """Login to Vault, returns the Vault token"""
    print(api.approle_login(**kwargs))


@vault.command()
@click.argument('PATH')
@click.argument('VALUES_JSON')
def read_env_vars(**kwargs):
    """Output Vault values as env vars"""
    api.read_env_vars(**kwargs)
