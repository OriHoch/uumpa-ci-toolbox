import tempfile
from ..common import check_call


def install(version, target_filename='/usr/local/bin/kubectl', with_sudo=False):
    with tempfile.TemporaryDirectory() as tempdir:
        check_call(['curl', '-Ls', 'https://storage.googleapis.com/kubernetes-release/release/{}/bin/linux/amd64/kubectl'.format(version), '-okubectl'], cwd=tempdir)
        check_call([*(['sudo'] if with_sudo else []), 'mv', '-f', 'kubectl', target_filename], cwd=tempdir)
        check_call(['chmod', '+x', target_filename], cwd=tempdir)
    check_call([target_filename, 'version', '--client'])
