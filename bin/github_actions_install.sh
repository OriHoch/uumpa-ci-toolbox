#!/usr/bin/env bash

COMMIT_SHA="${1}"
REPO="${2:-OriHoch/uumpa-ci-toolbox}"

pip install --upgrade pip &&\
pip install -r "https://raw.githubusercontent.com/${REPO}/${COMMIT_SHA}/requirements.txt" &&\
pip install --no-binary :all: "https://github.com/${REPO}/archive/${COMMIT_SHA}.zip#egg=uumpa-ci-toolbox"
