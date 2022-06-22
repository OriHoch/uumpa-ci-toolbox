import os

from ...git import api as git_api
from ... import common


def self_checkout(fetch_depth, path, config_user_name, config_user_email):
    if not path:
        path = os.path.abspath('.')
    tag_name = get_tag_name()
    git_api.checkout(
        github_repo_name=os.environ['GITHUB_REPOSITORY'],
        branch_name=get_branch_name() if not tag_name else None,
        tag_name=tag_name,
        fetch_depth=fetch_depth,
        github_token=os.environ['GITHUB_TOKEN'],
        path=path,
        config_user_name=config_user_name,
        config_user_email=config_user_email
    )


def get_tag_name():
    return git_api.get_tag_name(ref=os.environ['GITHUB_REF'])


def get_branch_name():
    return git_api.get_branch_name(ref=os.environ['GITHUB_REF'])


def docker_login():
    common.check_call('echo "{}" | docker login ghcr.io -u {} --password-stdin'.format(
        os.environ['GITHUB_TOKEN'], get_repo_owner()
    ), shell=True)


def get_repo_owner():
    return os.environ['GITHUB_REPOSITORY'].split('/')[0]
