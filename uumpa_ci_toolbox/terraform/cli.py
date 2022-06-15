import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def terraform():
    pass


@terraform.command()
@click.option('--version', required=True, help='Terraform version to install, e.g. "1.2.2"')
@click.option('--target-filename', default='/usr/local/bin/terraform')
@click.option('--with-sudo', is_flag=True)
def install(**kwargs):
    """Install Terraform in the given version"""
    api.install(**kwargs)
    common.cli_success()
