import os

from ruamel import yaml


def _update(values, set_values):
    for k, v in set_values.items():
        if v is None:
            if k in values:
                del values[k]
        elif isinstance(v, dict) and isinstance(values.get(k), dict):
            update(values[k], v)
        else:
            values[k] = v


def update(patch, yaml_file):
    if os.path.exists(yaml_file):
        with open(yaml_file) as f:
            values = yaml.safe_load(f)
    else:
        values = {}
    _update(values, patch)
    with open(yaml_file, "w") as f:
        yaml.safe_dump(values, f, default_flow_style=False)
