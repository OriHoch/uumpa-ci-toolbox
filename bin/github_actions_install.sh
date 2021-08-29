#!/usr/bin/env bash

COMMIT_SHA="${1}"

pip install --upgrade pip &&\
pip install -r "https://raw.githubusercontent.com/OriHoch/uumpa-ci-toolbox/${COMMIT_SHA}/requirements.txt" &&\
pip install "https://github.com/OriHoch/uumpa-ci-toolbox/archive/${COMMIT_SHA}.zip#egg=uumpa-ci-toolbox"