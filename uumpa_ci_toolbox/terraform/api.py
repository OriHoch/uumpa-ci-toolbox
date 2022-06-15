import tempfile
from ..common import check_call


def install(version, target_filename='/usr/local/bin/terraform', with_sudo=False):
    with tempfile.TemporaryDirectory() as tempdir:
        check_call(['curl', '-Ls', f'https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip', '-oterraform.zip'], cwd=tempdir)
        check_call(['unzip', 'terraform.zip'], cwd=tempdir)
        check_call([*(['sudo'] if with_sudo else []), 'mv', '-f', 'terraform', target_filename], cwd=tempdir)
        check_call(['chmod', '+x', target_filename], cwd=tempdir)
    check_call([target_filename, '-version'])
