import json

import click

from . import api
from .. import common


@click.group()
def yaml():
    pass


@yaml.command()
@click.argument('PATCH_JSON')
@click.argument('YAML_FILE')
def update(**kwargs):
    """Update a yaml file with the given json.

    Recursively replaces/adds attributes from the json to the yaml.
    If a value is null - deletes the attribute from the yaml."""
    kwargs['patch'] = json.loads(kwargs.pop('patch_json'))
    api.update(**kwargs)
    common.cli_success()
