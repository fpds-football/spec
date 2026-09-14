#!/bin/sh
# Build the public site for Cloudflare Workers static assets.
# Cloudflare Workers Builds: build command "sh scripts/build-site.sh", deploy command "npx wrangler deploy".
# The site contains only these paths. Do not publish the repository root.
set -eu

cd "$(dirname "$0")/.."

rm -rf _site
mkdir -p _site
cp index.html _headers _site/
cp -R schema consult _site/

echo "Built _site:"
find _site -type f | sort
