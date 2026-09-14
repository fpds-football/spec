#!/bin/sh
# Build the public site for Cloudflare Pages.
# Cloudflare Pages settings: build command "sh scripts/build-site.sh", output directory "_site".
# The site contains only these paths. Do not publish the repository root.
set -eu

cd "$(dirname "$0")/.."

rm -rf _site
mkdir -p _site
cp index.html _headers _site/
cp -R schema consult _site/

echo "Built _site:"
find _site -type f | sort
