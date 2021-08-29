import os
import base64
import tempfile
import subprocess
from contextlib import contextmanager

from uumpa_ci_toolbox import common


@contextmanager
def checkout(github_repo_name=None, branch_name=None, github_token=None, fetch_depth=1, ssh_key=None, ssh_key_file=None,
             config_user_name=None, config_user_email=None):
    assert github_repo_name, 'github repo name is required as no other git repository types are supported at the moment'
    assert branch_name, 'branch name is required'
    with tempfile.TemporaryDirectory() as tempdir:
        git_repo_path = os.path.join(tempdir, 'repo')
        common.check_call(['git', 'init', git_repo_path])
        if subprocess.call(['git', 'config', '--local', 'gc.auto', '0'], cwd=git_repo_path) != 0:
            print('WARNING! Failed to disable git garbage collection, fetch operation may cause a delay.')
        if github_token:
            assert not ssh_key, 'cannot set both github_token and ssh_key'
            common.check_call([
                'git', 'config', '--local', 'http.https://github.com/.extraheader', 'AUTHORIZATION: basic {}'.format(
                    base64.b64encode('x-access-token:{}'.format(github_token).encode()).decode()
                )
            ], cwd=git_repo_path)
            git_repo_url = 'https://github.com/{}'.format(github_repo_name)
        elif ssh_key or ssh_key_file:
            if ssh_key_file:
                assert not ssh_key
            else:
                assert ssh_key
                ssh_key_file = os.path.join(tempdir, 'ssh_key')
                with open(ssh_key_file, 'w') as f:
                    f.write(ssh_key)
            common.check_call(['chmod', '400', ssh_key_file])
            common.check_call([
                'git', 'config', '--local', 'core.sshCommand', 'ssh -i {} -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'.format(ssh_key_file)
            ], cwd=git_repo_path)
            git_repo_url = 'git@github.com:{}.git'.format(github_repo_name)
        else:
            git_repo_url = 'https://github.com/{}'.format(github_repo_name)
        if config_user_name:
            common.check_call([
                'git', 'config', '--local', 'user.name', config_user_name
            ])
        if config_user_email:
            common.check_call([
                'git', 'config', '--local', 'user.email', config_user_email
            ])
        common.check_call(['git', 'remote', 'add', 'origin', git_repo_url], cwd=git_repo_path)
        common.check_call(['git', 'fetch', '--depth', str(fetch_depth), 'origin', branch_name], cwd=git_repo_path)
        common.check_call(['git', 'checkout', branch_name], cwd=git_repo_path)
        yield git_repo_path


def get_tag_name(ref=None):
    if ref and ref.startswith('refs/tags/'):
        return ref.replace('refs/tags/', '')
    else:
        return None


def get_branch_name(ref=None):
    if ref and ref.startswith('refs/heads/'):
        return ref.replace('refs/heads/', '')
    else:
        return None


def get_last_commit_message():
    return subprocess.check_output(['git', 'log', '-1', '--pretty=format:%s']).decode()
