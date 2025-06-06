#!/usr/bin/env bash
set -e

# either set PYTHONPATH to include src --- or run from src directory
cd $(git rev-parse --show-toplevel)
cd src


export XRA_API_PORT=$(python3 -c "from xra.central_config import dfcc; print(dfcc.api_port)")
export XRA_API_HOST=$(python3 -c "from xra.central_config import dfcc; print(dfcc.api_host)")

printf "Starting Uvicorn server at http://$XRA_API_HOST:$XRA_API_PORT\n\n"

export PIPENV_VERBOSITY="-1"
pipenv run uvicorn main_api:app --port $XRA_API_PORT --host $XRA_API_HOST



# --host       Host to bind to (default: 127.0.0.1)
# --port       Port to bind to (default: 8000)
# --workers    Number of worker processes (used in production)
# --log-level  Logging level (info, debug, warning, error, critical)  # default: info

# --reload     Automatically reload server on code changes (for development)
# i think you can limit this to a specific directory with --reload-dir
