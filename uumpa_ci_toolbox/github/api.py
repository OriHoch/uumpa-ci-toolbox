import os
import tempfile
from base64 import b64encode

import requests
from nacl import encoding, public

from ..ssh import api as ssh_api


def assert_github_token():
    github_token = os.environ.get('GITHUB_TOKEN')
    assert github_token, 'missing GITHUB_TOKEN'
    return github_token


def create_deploy_key(repository, key_title, public_key, read_only):
    res = requests.post('https://api.github.com/repos/{}/keys'.format(repository), json={
        'title': key_title,
        'key': public_key,
        'read_only': read_only
    }, headers={'Authorization': 'token {}'.format(assert_github_token())})
    res.raise_for_status()
    return res.json()


def add_environment_secret(repository, key, value):
    res = requests.get(
        'https://api.github.com/repos/{}/actions/secrets/public-key'.format(repository), json={},
        headers={'Authorization': 'token {}'.format(assert_github_token())}
    ).json()
    repo_public_key = res['key']
    repo_public_key_id = res['key_id']
    public_key = public.PublicKey(repo_public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(value.encode("utf-8"))
    encrypted_value = b64encode(encrypted).decode("utf-8")
    requests.put(
        'https://api.github.com/repos/{}/actions/secrets/{}'.format(repository, key),
        json={'encrypted_value': encrypted_value, 'key_id': repo_public_key_id},
        headers={'Authorization': 'token {}'.format(assert_github_token())}
    ).raise_for_status()


def create_and_configure_deploy_key(create_deploy_key_repository, add_environment_secret_repository, deploy_key_title, environment_secret_name):
    with tempfile.TemporaryDirectory() as tempdir:
        key_filename = os.path.join(tempdir, 'id_rsa')
        ssh_api.key_gen(deploy_key_title, key_filename)
        pubkey_filename = os.path.join(tempdir, 'id_rsa.pub')
        with open(pubkey_filename) as f:
            public_key = f.read()
        create_deploy_key(create_deploy_key_repository, deploy_key_title, public_key, read_only=False)
        with open(key_filename) as f:
            private_key = f.read()
        add_environment_secret(add_environment_secret_repository, environment_secret_name, private_key)
