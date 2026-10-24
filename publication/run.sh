#!/bin/sh
# Thin consumer entry. No compiler, candidate or evidence logic lives here.
set -eu
if [ "$#" -lt 3 ] || [ "$1" != "--engine" ]; then
  echo 'Usage: sh publication/run.sh --engine /path/to/publication-engine preview|candidate|doctor ...' >&2
  exit 2
fi
engine=$2
shift 2
base=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
exec uv run --project "$engine" --locked --group review python -B \
  "$engine/engine/pub.py" --project "$base/standalone.json" "$@"
