#!/usr/bin/env bash
git pull || exit 1
python3 manage.py makemigrations
python3 manage.py collectstatic <<< yes
