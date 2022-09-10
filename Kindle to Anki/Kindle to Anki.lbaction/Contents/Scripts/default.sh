#!/bin/sh
#
# LaunchBar Action Script
#

export LANG="en_US.UTF-8"

echo "$# arguments passed"

for ARG in "$@"; do
    cat "$ARG" \
    | sed -E "s/^(.*)/MINJAISRICH\1/g" \
    | tr -d "\r\n" \
    | perl -pe "s/MINJAISRICH(.*?)\s\((.*?)\)MINJAISRICH.*?添加于(.*?年.*?月.*?日).*?MINJAISRICHMINJAISRICH(.*?)MINJAISRICH==========/\4;\2：《\1》;\3\n/g" > "$ARG.md"
done