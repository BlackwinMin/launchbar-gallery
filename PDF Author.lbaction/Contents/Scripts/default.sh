#!/bin/sh
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

read -r -d '' applescriptCode1 <<'EOF'
    set f to text returned of (display dialog "请输入作者名" default answer "")
    return f
EOF
authorName=$(osascript -e "$applescriptCode1")

exiftool -Author="$authorName" "$@" -overwrite_original