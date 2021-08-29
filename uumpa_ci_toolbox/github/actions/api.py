import os

from ...git import api as git_api
from ... import common


def self_checkout(fetch_depth, path):
    if not path:
        path = os.path.abspath('.')
    git_api.checkout(
        github_repo_name=os.environ['GITHUB_REPOSITORY'],
        branch_name=get_branch_name(),
        fetch_depth=fetch_depth,
        github_token=os.environ['GITHUB_TOKEN'],
        path=path
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
