import click

from . import api
from .. import common


@click.group()
def ssh():
    pass


@ssh.command()
@click.option('--comment', required=True, help="Public key comment")
@click.option('--filename', required=True, help="Path to the private key to create, public key will use the same filename with .pub suffix")
def key_gen(**kwargs):
    """Generate an SSH public/private key pair"""
    api.key_gen(**kwargs)
    common.cli_success()
