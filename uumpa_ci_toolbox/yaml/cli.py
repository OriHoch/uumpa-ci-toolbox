import json

import click

from . import api


@click.group()
def yaml():
    pass


@yaml.command()
@click.argument('PATCH_JSON')
@click.argument('YAML_FILE')
def update(**kwargs):
    kwargs['patch'] = json.loads(kwargs.pop('patch_json'))
    api.update(**kwargs)
