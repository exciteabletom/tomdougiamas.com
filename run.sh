#!/usr/bin/env bash
# Start the project in production mode

# Go to project root
command cd "$(dirname "$0")" || exit 1

. .venv/bin/activate

export PERSONAL_SITE_PRODUCTION_MODE=yes
gunicorn --error-logfile errors.txt --workers 2 --bind unix:tomdougiamas.com.sock -m 007 personal_site.wsgi

