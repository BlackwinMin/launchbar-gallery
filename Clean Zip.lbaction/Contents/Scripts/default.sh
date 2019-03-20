#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"
for ARG in "$@"; do
    zip -q -d "$ARG" *__MACOSX* || true
    zip -q -d "$ARG" \*.DS_Store || true
done && afplay "/System/Library/Sounds/Submarine.aiff"