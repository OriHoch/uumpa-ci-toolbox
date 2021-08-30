import click

from . import api
from .. import common


@click.group()
def git():
    pass


@git.command()
@click.option('--github-repo-name', required=True, help='in the format of owner/repo (e.g. "OriHoch/uumpa-ci-toolbox")')
@click.option('--branch-name', required=True)
@click.option('--github-token', help='GitHub personal access token to authenticate for write access')
@click.option('--fetch-depth', default=1, help='How many commits to fetch')
@click.option('--ssh-key', help='content of private ssh key which can be used for write access to the repo')
@click.option('--ssh-key-file', help='path to private ssh key which can be used for write access to the repo')
@click.option('--path', required=True, help='target path for the checkout')
@click.option('--config-user-name', help='configure the user name used when making commits from the repo')
@click.option('--config-user-email', help='configure the user email used when making commits, if user-name is provided it will default to "user-name@localhost"')
def checkout(**kwargs):
    """Checkout a Git repository and optionally make it available for editing"""
    api.checkout(**kwargs)
    common.cli_success()


@git.command()
@click.option('--ref', required=True, help='Git ref (e.g. "refs/tags/v1.2.3" will return "v1.2.3")')
def get_tag_name(**kwargs):
    """Get the tag name from a Git ref"""
    tag_name = api.get_tag_name(**kwargs)
    if tag_name is not None:
        print(tag_name)


@git.command()
@click.option('--ref', required=True, help='Git ref (e.g. "refs/heads/main" will return "main")')
def get_branch_name(**kwargs):
    """Get the branch name from a Git ref"""
    branch_name = api.get_branch_name(**kwargs)
    if branch_name is not None:
        print(branch_name)


@git.command()
def get_last_commit_message():
    """Get the last commit message"""
    print(api.get_last_commit_message())


@git.command()
@click.option('--equals', help="Commit message equals to this specified string")
@click.option('--starts-with', help="Commit message starts with this specified string")
@click.option('--contains', help="Commit message contains this specified string")
def check_last_commit_message(**kwargs):
    """Check the last commit message for specified strings

    If any of the options match - it will exit with returncode 0,
    otherwise it will exit with returncode 1"""
    exit(0 if api.check_last_commit_message(**kwargs) else 1)
