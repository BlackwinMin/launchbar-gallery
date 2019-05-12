#!/bin/sh
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

read -r -d '' applescriptCode1 <<'EOF'
    set imgWidth to text returned of (display dialog "请输入向右移动的宽度" default answer "100")
    return imgWidth
EOF
imgWidth=$(osascript -e "$applescriptCode1")

for f in "$@";do
    w=$(convert "$f" -print "%w\n" /dev/null || true)
    h=$(convert "$f" -print "%h\n" /dev/null || true)
    if [ "$w" -gt "$h" ]
    then
        imageBelow="$f"
        imageBelowwidth="$w"
    else
        imageUp="$f"
    fi
done

ddate=`date +%Y-%m-%d-%H%M%S`
let canvasWidth=$imageBelowwidth+$imgWidth
convert "$imageBelow" -background transparent -extent "$canvasWidth" "/Users/apple/Desktop/temp_minja.png"

composite -gravity southeast "$imageUp" "/Users/apple/Desktop/temp_minja.png" "/Users/apple/Desktop/overlay-$ddate.png" && rm "/Users/apple/Desktop/temp_minja.png"