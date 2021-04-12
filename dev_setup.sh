#!/usr/bin/bash

# Go to project root
command cd "$(dirname "$0")" || exit 1

if ! find . | grep --quiet .venv/bin/activate; then
  python3 -m venv .venv
fi

. .venv/bin/activate

python3 -m pip install --upgrade pip wheel
python3 -m pip install -r requirements.txt -r requirements-dev.txt

pre-commit install
pre-commit run
