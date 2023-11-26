#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python ./www/manage.py collectstatic --no-input
python ./www/manage.py migrate