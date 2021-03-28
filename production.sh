#!/usr/bin/env bash

# Go to project root
cd "$(dirname "$0")"

# Enable production mode
command sed -i 's/PRODUCTION_ENABLED = True/PRODUCTION_ENABLED = False/' personal_site/settings.py
