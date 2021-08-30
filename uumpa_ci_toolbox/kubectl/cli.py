import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def kubectl():
    pass


@kubectl.command()
@click.option('--version', required=True, help='Kubectl version to install, e.g. "v1.19.0"')
@click.option('--target-filename', default='/usr/local/bin/kubectl')
@click.option('--with-sudo', is_flag=True)
def install(**kwargs):
    """Install Kubectl in the given version"""
    api.install(**kwargs)
    common.cli_success()
