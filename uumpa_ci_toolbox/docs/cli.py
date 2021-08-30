import click

from . import api
from .. import common


@click.group()
def docs():
    pass


@docs.command()
@click.option('--python-venv', help='path to Python virtualenv which has the relevant click cli')
@click.option('--cli-command', required=True, help='the name of the relevant click cli command binary')
@click.option('--cli-module', required=True, help='the main cli module name (e.g. "uumpa_ci_toolbox.cli")')
@click.option('--main-command', required=True, help='the main command within the cli module (e.g. "main")')
@click.option('--output-file', required=True, help='path to the markdown file to update with the rendered documentation')
@click.option('--start-line-contains', required=True, help='comment within the markdown file that marks the start of the documentation')
@click.option('--end-line-contains', required=True, help='comment within the markdown file that marks the end of the documentation')
def render_markdown_from_click_cli(**kwargs):
    """Generate markdown documentation from a click cli command"""
    api.render_markdown_from_click_cli(**kwargs)
    common.cli_success()
