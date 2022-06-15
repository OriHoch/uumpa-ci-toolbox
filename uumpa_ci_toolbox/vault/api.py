import os
import tempfile
from ..common import check_call, check_output_json


def install(version, target_filename='/usr/local/bin/vault', with_sudo=False):
    with tempfile.TemporaryDirectory() as tempdir:
        check_call(['curl', '-Ls', f'https://releases.hashicorp.com/vault/{version}/vault_{version}_linux_amd64.zip', '-ovault.zip'], cwd=tempdir)
        check_call(['unzip', 'vault.zip'], cwd=tempdir)
        check_call([*(['sudo'] if with_sudo else []), 'mv', '-f', 'vault', target_filename], cwd=tempdir)
        check_call(['chmod', '+x', target_filename], cwd=tempdir)
    check_call([target_filename, '-version'])


def create_approle(role, policy):
    assert os.environ.get('VAULT_ADDR'), 'missing VAULT_ADDR env var containing the URL to the Vault instance'
    assert os.environ.get('VAULT_TOKEN'), 'missing VAULT_TOKEN env var containing the Vault token'
    check_call([
        'vault', 'write', f'auth/approle/role/{role}',
        f'token_policies="{policy}"', 'token_ttl=1h', 'token_max_ttl=4h'
    ])
    role_id = check_output_json(['vault', 'read', f'auth/approle/role/{role}/role-id', '-format=json'])['data']['role_id']
    secret_id = check_output_json(['vault', 'write', '-force', f'auth/approle/role/{role}/secret-id', '-format=json'])['data']['secret_id']
    return {'role_id': role_id, 'secret_id': secret_id}


def approle_login(role_id, secret_id):
    assert os.environ.get('VAULT_ADDR'), 'missing VAULT_ADDR env var containing the URL to the Vault instance'
    return check_output_json(['vault', 'write', 'auth/approle/login', f'role_id={role_id}', f'secret_id={secret_id}', '-format=json'])['auth']['client_token']
