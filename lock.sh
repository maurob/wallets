#!/bin/sh

if [ -n "$VIRTUAL_ENV" ]; then
    pip freeze | sed '/^wallets/ s/.*/./' > requirements.lock
    # It also replaces the local project python package with the currentpath ".",
    # to avoid absolute local filesystem referencies.
else
    echo "You have to run this script with an activated virtualenv."
fi
