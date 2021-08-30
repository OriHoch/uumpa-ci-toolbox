import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def minikube():
    pass


@minikube.command()
@click.option('--version', required=True, help='Minikube version to install, e.g. "v1.21.0"')
@click.option('--target-filename', default='/usr/local/bin/minikube')
@click.option('--with-sudo', is_flag=True)
def install(**kwargs):
    """Install Minikube in the given version"""
    api.install(**kwargs)
    common.cli_success()
