#!/usr/bin/env bash

# Go to project root
cd "$(dirname "$0")"

# Enable production mode
command sed -i 's/PRODUCTION_ENABLED = False/PRODUCTION_ENABLED = True/' personal_site/settings.py
