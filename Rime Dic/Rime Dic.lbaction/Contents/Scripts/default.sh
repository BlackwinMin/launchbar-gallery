#!/bin/sh
#
# LaunchBar Action Script
#

cd /Users/apple/Library/Rime
echo "$# arguments passed"
for ARG in "$@"; do
#    echo "${ARG/ /\t}" >> luna_pinyin.extended.dict.yaml
    echo "${ARG/ /\t}" >> custom_phrase.txt
done