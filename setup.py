from setuptools import setup, find_packages
from os import path
import time

if path.exists("VERSION.txt"):
    # this file can be written by CI tools (e.g. Travis)
    with open("VERSION.txt") as version_file:
        version = version_file.read().strip().strip("v")
else:
    version = str(time.time())

setup(
    name='uumpa-ci-toolbox',
    version=version,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    entry_points={
        'console_scripts': [
            'uci = uumpa_ci_toolbox.cli:main',
        ]
    },
)
