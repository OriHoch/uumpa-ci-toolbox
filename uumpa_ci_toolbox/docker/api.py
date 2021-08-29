import subprocess

from uumpa_ci_toolbox import common


def build_cache(cache_from, docker_build_args):
    if subprocess.call(['docker', 'pull', cache_from]) == 0:
        cache_from_args = ['--cache-from', cache_from]
    else:
        cache_from_args = []
    common.check_call(['docker', 'build', *cache_from_args, *docker_build_args])


def tag_push(source_tag_name, push_tag_name):
    common.check_call(['docker', 'tag', source_tag_name, push_tag_name])
    common.check_call(['docker', 'push', push_tag_name])
