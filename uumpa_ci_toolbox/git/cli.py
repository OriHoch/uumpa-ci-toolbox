import click

from . import api


@click.group()
def git():
    pass


@git.command()
@click.option('--github-repo-name')
@click.option('--branch-name')
@click.option('--github-token')
@click.option('--fetch-depth', default=1)
@click.option('--ssh-key')
@click.option('--ssh-key-file')
@click.option('--path')
def checkout(**kwargs):
    api.checkout(**kwargs)


@git.command()
@click.option('--ref')
def get_tag_name(**kwargs):
    tag_name = api.get_tag_name(**kwargs)
    if tag_name is not None:
        print(tag_name)


@git.command()
@click.option('--ref')
def get_branch_name(**kwargs):
    branch_name = api.get_branch_name(**kwargs)
    if branch_name is not None:
        print(branch_name)


@git.command()
def get_last_commit_message():
    print(api.get_last_commit_message())
