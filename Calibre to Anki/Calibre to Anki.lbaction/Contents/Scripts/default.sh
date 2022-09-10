#!/bin/sh
#
# LaunchBar Action Script
#

export LANG="en_US.UTF-8"

for ARG in "$@"; do
    
    tTitle=`cat "$ARG" | head -1 | sed 's/^....//'`
    
    cat "$ARG" \
    | sed '1d' \
    | sed '/^###/d' \
    | sed -E "s/^(.*)/MINJAISRICH\1/g" \
    | tr -d "\r\n" \
    | perl -pe "s/MINJAISRICHMINJAISRICH(.*?)MINJAISRICH\[(.*?)\]\((.*?)\)MINJAISRICHMINJAISRICH-+/\1;$tTitle;\2;\3\n/g"\
    | sed -E "s/^MINJAISRICH(.*)/\1/g" > "$ARG.md"
done