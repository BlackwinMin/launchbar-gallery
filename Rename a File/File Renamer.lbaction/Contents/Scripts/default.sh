#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"

v="$@"
read -r -d '' applescriptCode <<'EOF'
	on run argv
		set r to text returned of (display dialog "Please input new file name" default answer argv)
		return r
	end run
EOF
r=$(osascript -e "$applescriptCode" "$v")

for f in "$@";do
	mv "$f" "$r"
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"renamed to  $r\" with title \"File Renamer\""