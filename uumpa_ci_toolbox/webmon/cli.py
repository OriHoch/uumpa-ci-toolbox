import click

from . import api


@click.group()
def webmon():
    pass


@webmon.command()
@click.argument('PORT')
@click.argument('PYTHON_CODE')
def start(**kwargs):
    """Starts a web service which runs the given python_code on each request.

    This is useful for monitoring things, a web monitoring service can be connected to it
    and alert on abstract conditions

    The python_code should define a webmon() function which returns a tuple of (boolean, dict)

    All code, including imports should be within the webmon function

    python_code example:

    def webmon():
      import random
      if random.randint(0,1):
        return True, {'hello': 'world'}
      else:
        return False, {'error': 'failed'}
    """
    api.start(**kwargs)


@webmon.command()
@click.argument('PORT')
@click.argument('CONFIG_FILE')
def start_multi(**kwargs):
    """Starts multiple webmon services listening on the same port based on a yaml config file

    Example config file:

    webmons:
      - path: /random
        # all code, including imports should be within the webmon function
        python_code: |
          def webmon():
            import random
            if random.randint(0,1):
              return True, {'hello': 'world'}
            else:
              return False, {'error': 'failed'}
      - path: /test
        # all code, including imports should be within the webmon function
        python_file: /path/to/my_code.py
    """
    api.start_multi(**kwargs)
