#!/usr/bin/env bash

# Go to project root
command cd "$(dirname "$0")" || exit 1

git pull || exit 1
python3 manage.py makemigrations
python3 manage.py collectstatic <<< yes
