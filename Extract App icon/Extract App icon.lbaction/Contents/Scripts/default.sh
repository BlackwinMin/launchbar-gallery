#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"
for ARG in "$@"; do
    appIcon=`defaults read "$ARG"/Contents/Info.plist CFBundleIconFile`
    appName=`basename "$ARG"`
    if [[ "$appIcon" == *icns ]]; then
        iconPath="$ARG"/Contents/Resources/"$appIcon"
    else
        iconPath="$ARG"/Contents/Resources/"$appIcon".icns
    fi

    sips -s format png --out "/Users/apple/Desktop/$appName.png" "$iconPath"
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 导出 icon 成功)\""