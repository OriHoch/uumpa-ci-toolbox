import click

from . import api


@click.group()
def actions():
    pass


@actions.command()
@click.option('--fetch-depth', default=1)
@click.option('--path')
def self_checkout(**kwargs):
    api.self_checkout(**kwargs)


@actions.command()
def get_tag_name():
    tag_name = api.get_tag_name()
    if tag_name is not None:
        print(tag_name)


@actions.command()
def get_branch_name():
    branch_name = api.get_branch_name()
    if branch_name is not None:
        print(branch_name)


@actions.command()
def docker_login():
    api.docker_login()
