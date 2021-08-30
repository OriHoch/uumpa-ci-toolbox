import click


from .git.cli import git
from .github.cli import github
from .docker.cli import docker
from .yaml.cli import yaml
from .ssh.cli import ssh
from .docs.cli import docs
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


@main.command()
def version():
    """Print the Uumpa CI Toolbox version"""
    print(version.UCI_VERSION)
