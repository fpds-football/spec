#!/bin/sh
# Build the files that this repository publishes: the schema only (DECISIONS.md D-41).
# Cloudflare Workers Builds: build command "sh scripts/build-site.sh", deploy command "npx wrangler deploy".
# fpds-football/site publishes every other path on fpds.football.
set -eu

cd "$(dirname "$0")/.."

rm -rf _site
mkdir -p _site
cp _headers _site/
cp -R schema _site/

echo "Built _site:"
find _site -type f | sort
