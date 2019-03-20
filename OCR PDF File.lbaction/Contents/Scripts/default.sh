#!/bin/bash
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

echo "$# arguments passed"

for f in "$@"; do
    ocrmypdf "$f" "$f" -l chi_sim+eng --force-ocr
done && afplay "/System/Library/Sounds/Submarine.aiff"