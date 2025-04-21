#!/usr/bin/env bash

COMMIT_SHA="${1}"
REPO="${2:-OriHoch/uumpa-ci-toolbox}"

export PIP_USE_PEP517=0

pip install --upgrade pip setuptools wheel &&\
pip install -r "https://raw.githubusercontent.com/${REPO}/${COMMIT_SHA}/requirements.txt" &&\
pip install "https://github.com/${REPO}/archive/${COMMIT_SHA}.zip#egg=uumpa-ci-toolbox"
