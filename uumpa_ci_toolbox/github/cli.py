import json

import click

from .actions.cli import actions
from . import api
from .. import common


@click.group()
def github():
    pass


github.add_command(actions)


@github.command()
@click.option('--repository', required=True, help='GitHub repository name (owner/name)')
@click.option('--key-title', required=True, help="Title of the deploy key, will be shown on GitHub deploy keys UI")
@click.option('--public-key', required=True, help="Content of the SSH public key of the deploy key")
@click.option('--read-only', is_flag=True, help="If true, will set the key as read-only")
def create_deploy_key(**kwargs):
    """Add a deploy key to a GitHub repo

    Required GITHUB_TOKEN environment variable to be set with a GitHub personal access token"""
    print(json.dumps(api.create_deploy_key(**kwargs)))
    common.cli_success()


@github.command()
@click.option('--repository', required=True, help='GitHub repository name (owner/name)')
@click.option('--key', required=True, help="Secret name")
@click.option('--value', required=True, help="Secret value")
def add_environment_secret(**kwargs):
    """Add an environment secret to a GitHub repo

    Required GITHUB_TOKEN environment variable to be set with a GitHub personal access token"""
    api.add_environment_secret(**kwargs)
    common.cli_success()


@github.command()
@click.option('--create-deploy-key-repository', required=True, help="Will add the deploy key to this repository")
@click.option('--add-environment-secret-repository', required=True, help="Will add the environment secret to this repository")
@click.option('--deploy-key-title', required=True, help="Title of the deploy key, displayed on GitHub UI")
@click.option('--environment-secret-name', required=True, help="Name of the environment secret")
def create_and_configure_deploy_key(**kwargs):
    """Create and configure a deploy key from one repository to a different repository.

    This will allow the repository specified in "--add-environment-secret-repository" to make changes in
    the repository specified in "--create-deploy-key-repository" by using git checkout with the ssh key
    that will be defined in the environment secret.

    Required GITHUB_TOKEN environment variable to be set with a GitHub personal access token with appropriate
    permissions to both repositories"""
    api.create_and_configure_deploy_key(**kwargs)
    common.cli_success()