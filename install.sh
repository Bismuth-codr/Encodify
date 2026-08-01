#!/usr/bin/env bash
set -e

chmod +x ecode

sudo ln -sf "$(pwd)/ecode" /usr/local/bin/ecode

echo "Installed ecode!"
