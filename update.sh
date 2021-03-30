#!/usr/bin/env bash

# Go to project root
command cd "$(dirname "$0")" || exit 1

git pull || exit 1
python3 manage.py makemigrations

# Django doesn't register if a file is deleted from project static folders
command rm -rf ./static/
python3 manage.py collectstatic <<< yes
