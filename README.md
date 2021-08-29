# Uumpa CI Toolbox

A set of tools (AKA toolbox) for running continuous integration workflows.

## Goals

* Python as the primary language of the tools
* No vendor lock, but can have tools to allow support of specific vendors

## Local Development

### Install

Create Python 3.8 virtualenv

```
python3.8 -m venv venv
```

Upgrade pip

```
venv/bin/pip install --upgrade pip
```

Install dependencies

```
venv/bin/pip install -r requirements.txt
```

Install package

```
venv/bin/pip install -e .
```

### Use

Activate virtualenv

```
. venv/bin/activate
```

See help message for available commands

```
uci --help
```