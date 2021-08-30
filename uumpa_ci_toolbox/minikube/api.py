import tempfile
from ..common import check_call


def install(version, target_filename='/usr/local/bin/minikube', with_sudo=False):
    with tempfile.TemporaryDirectory() as tempdir:
        check_call(['curl', '-Ls', 'https://github.com/kubernetes/minikube/releases/download/{}/minikube-linux-amd64.tar.gz'.format(version), '-ominikube.tar.gz'], cwd=tempdir)
        check_call(['tar', '-xzvf', 'minikube.tar.gz'], cwd=tempdir)
        check_call([*(['sudo'] if with_sudo else []), 'mv', '-f', 'out/minikube-linux-amd64', target_filename], cwd=tempdir)
        check_call(['chmod', '+x', target_filename], cwd=tempdir)
    check_call([target_filename, 'version'])
