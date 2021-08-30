import click

from uumpa_ci_toolbox import common

from . import api


@click.group()
def util():
    """Misc. utilities and helper commands"""
    pass


@util.command()
@click.option('--timeout-seconds', required=True, type=int)
@click.option('--timeout-message')
@click.argument('CONDITION_SCRIPT')
def wait_for(timeout_seconds, timeout_message, condition_script):
    """Calls the condition script every second until it exits with returncode 0"""
    if api.wait_for(timeout_seconds, condition_script):
        common.cli_success()
    else:
        print(timeout_message if timeout_message else 'Wait too long for condition')
        exit(1)
