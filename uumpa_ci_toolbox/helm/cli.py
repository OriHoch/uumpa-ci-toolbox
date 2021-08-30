import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def helm():
    pass


@helm.command()
@click.option('--version', required=True, help='Helm version to install, e.g. "v3.2.4"')
@click.option('--target-filename', default='/usr/local/bin/helm')
@click.option('--with-sudo', is_flag=True)
def install(**kwargs):
    """Install Helm client in the given version"""
    api.install(**kwargs)
    common.cli_success()
