#!/bin/bash

set -ex

# Create a temporary directory
rm -rf tmp_build/
mkdir tmp_build/

# Copy all files to the temporary directory
cp -r static/ *.md *.py *.toml tmp_build/

# Change to the temporary directory
cd tmp_build

# Run the build steps
python3 parse_harmonic_bookmarks.py static/HarmonicBookmarks*.txt
python3 parse_claw_bookmarks.py
python3 parse_hn_bookmarks.py
git clone --recurse-submodules --depth 1 https://github.com/dipeshkaphle/dipeshkaphle.github.io
cp -r dipeshkaphle.github.io/templates templates && rm templates/index.html
mv dipeshkaphle.github.io/themes .
# rm -rf dipeshkaphle.github.io
mkdir content
printf "+++
title=  \"Learning\"
+++
" > content/_index.md
find . -maxdepth 1 -regextype posix-egrep -regex ".*\.(md|MD)" -exec cp "{}" content \;

# The zola build command is assumed to be `zola build`. 
# If this is incorrect, please modify the script.
if command -v zola &> /dev/null
then
    zola serve
else
    echo "Zola is not installed. Please install it to build the site."
    exit 1
fi
