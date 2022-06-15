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
