import click


from .git.cli import git
from .github.cli import github
from .docker.cli import docker
from .yaml.cli import yaml
from .ssh.cli import ssh
from .docs.cli import docs
from .helm.cli import helm
from .minikube.cli import minikube
from .util.cli import util
from .kubectl.cli import kubectl
from .webmon.cli import webmon
from .vault.cli import vault
from .terraform.cli import terraform
from . import version


@click.group(context_settings={'max_content_width': 120})
def main():
    """Uumpa CI Toolbox"""
    pass


main.add_command(git)
main.add_command(github)
main.add_command(docker)
main.add_command(yaml)
main.add_command(ssh)
main.add_command(docs)
main.add_command(helm)
main.add_command(minikube)
main.add_command(util)
main.add_command(kubectl)
main.add_command(webmon)
main.add_command(vault)
main.add_command(terraform)


@main.command()
def version():
    """Print the Uumpa CI Toolbox version"""
    print(version.UCI_VERSION)
