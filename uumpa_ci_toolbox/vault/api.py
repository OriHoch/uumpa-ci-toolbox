import tempfile
from ..common import check_call


def install(version, target_filename='/usr/local/bin/vault', with_sudo=False):
    with tempfile.TemporaryDirectory() as tempdir:
        check_call(['curl', '-Ls', f'https://releases.hashicorp.com/vault/{version}/vault_{version}_linux_amd64.zip', '-ovault.zip'], cwd=tempdir)
        check_call(['unzip', 'vault.zip'], cwd=tempdir)
        check_call([*(['sudo'] if with_sudo else []), 'mv', '-f', 'vault', target_filename], cwd=tempdir)
        check_call(['chmod', '+x', target_filename], cwd=tempdir)
    check_call([target_filename, '-version'])
