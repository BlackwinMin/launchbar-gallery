# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

read -r -d '' applescriptCode1 <<'EOF'
    set imgWidth to text returned of (display dialog "请输入图片宽度" default answer "900")
    return imgWidth
EOF

imgWidth=$(osascript -e "$applescriptCode1")


if [ -z $imgWidth ]
then
    osascript -e 'display notification with title "未指定分辨率" sound name "Pop"'
else
    for ARG in "$@"; do
        convert -resize $imgWidth "$ARG" "$ARG"
    done && afplay "/System/Library/Sounds/Submarine.aiff"
fi