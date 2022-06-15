import json
import subprocess


def check_call(*args, **kwargs):
    return_code = subprocess.call(*args, **kwargs)
    if return_code != 0:
        exit(return_code)


def cli_success():
    print('OK')
    exit(0)


def check_output_json(*args, **kwargs):
    return json.loads(subprocess.check_output(*args, **kwargs))
