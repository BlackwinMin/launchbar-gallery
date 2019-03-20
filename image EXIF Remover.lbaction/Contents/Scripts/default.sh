#!/bin/sh
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

idx=0

for f in "$@";do
    mogrify -strip "$f"
    let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 修改了 $idx 个文件)\""