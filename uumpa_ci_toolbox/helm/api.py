import tempfile
from ..common import check_call


def install(version, target_filename='/usr/local/bin/helm', with_sudo=False):
    with tempfile.TemporaryDirectory() as tempdir:
        check_call(['curl', '-Ls', 'https://get.helm.sh/helm-{}-linux-amd64.tar.gz'.format(version), '-ohelm.tar.gz'], cwd=tempdir)
        check_call(['tar', '-xzvf', 'helm.tar.gz'], cwd=tempdir)
        check_call([*(['sudo'] if with_sudo else []), 'mv', '-f', 'linux-amd64/helm', target_filename], cwd=tempdir)
        check_call(['chmod', '+x', target_filename], cwd=tempdir)
    check_call([target_filename, 'version', '--client'])
