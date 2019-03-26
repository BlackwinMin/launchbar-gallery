#!/bin/sh
#
# LaunchBar Action Script
#

cd /Users/apple/Library/Rime
echo "$# arguments passed"
LOWERCASE=$(echo "$@" | tr '[A-Z]' '[a-z]')
#echo "$@\t$LOWERCASE" >> luna_pinyin.extended.dict.yaml && afplay "/System/Library/Sounds/Submarine.aiff"
echo "$@\t$LOWERCASE" >> custom_phrase.txt && afplay "/System/Library/Sounds/Submarine.aiff"