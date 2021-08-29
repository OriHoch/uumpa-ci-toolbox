import os
from contextlib import contextmanager

from ...git import api as git_api
from ... import common


@contextmanager
def self_checkout(fetch_depth):
    with git_api.checkout(
        github_repo_name=os.environ['GITHUB_REPOSITORY'],
        branch_name=get_branch_name(),
        fetch_depth=fetch_depth,
        github_token=os.environ['GITHUB_TOKEN']
    ) as repodir:
        yield repodir


def get_tag_name():
    return git_api.get_tag_name(ref=os.environ['GITHUB_REF'])


def get_branch_name():
    return git_api.get_branch_name(ref=os.environ['GITHUB_REF'])


# TODO: make it stateless, currently the docker login/logout are global for the user session
@contextmanager
def docker_login():
    # echo "${GITHUB_TOKEN}" | docker login docker.pkg.github.com -u hasadna --password-stdin &&\
    common.check_call('echo "{}" | dokcer login ghcr.io -u {} --password-stdin'.format(
        os.environ['GITHUB_TOKEN'], get_repo_owner()
    ))
    try:
        yield
    finally:
        common.check_call(['docker', 'logout', 'ghcr.io'])


def get_repo_owner():
    return os.environ['GITHUB_REPOSITORY'].split('/')[0]
