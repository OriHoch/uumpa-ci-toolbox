import click

from . import api


@click.group()
def actions():
    """Commands that should be run from GitHub actions scripts.

    All commands depend on GitHub actions environment variables to be set.

    Some commands require GITHUB_TOKEN environment variable which should be set in the actions yaml script env as:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    """
    pass


@actions.command()
@click.option('--fetch-depth', default=1, help="How many commits to fetch")
@click.option('--path', help="Path to checkout to, defaults to current directory")
@click.option('--config-user-name', help="User name used to make commits")
@click.option('--config-user-email', help="User email used to make commits, defaults to user-name@localhost")
def self_checkout(**kwargs):
    """Checkout the repository which is currently running this GitHub actions script"""
    api.self_checkout(**kwargs)


@actions.command()
def get_tag_name():
    """Get the tag name of the currently running action"""
    tag_name = api.get_tag_name()
    if tag_name is not None:
        print(tag_name)


@actions.command()
def get_branch_name():
    """Get the branch name of the currently running action"""
    branch_name = api.get_branch_name()
    if branch_name is not None:
        print(branch_name)


@actions.command()
def docker_login():
    """Login to ghcr.io allowing to push images to the GitHub container registry for the current repository"""
    api.docker_login()
