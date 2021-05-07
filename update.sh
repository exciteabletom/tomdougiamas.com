#!/usr/bin/env bash
# Get latest changes from git and prepare static files for production

# Go to project root
command cd "$(dirname "$0")" || exit 1

export PERSONAL_SITE_PRODUCTION_MODE=yes

git pull || exit 1

python3 manage.py migrate

command rm -rf static
python3 manage.py collectstatic <<< yes
#python3 manage.py compress

sudo systemctl restart tomdougiamas.com