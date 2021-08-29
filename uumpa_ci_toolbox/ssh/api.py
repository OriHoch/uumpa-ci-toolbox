from .. import common


def key_gen(comment, filename):
    common.check_call(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-C', comment, '-f', filename, '-N', ''])
