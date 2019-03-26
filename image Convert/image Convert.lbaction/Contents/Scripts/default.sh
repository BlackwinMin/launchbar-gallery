#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"

read -r -d '' applescriptCode1 <<'EOF'
	tell application "System Events"
	set activeApp to name of first application process whose frontmost is true
	activate
	set formatList to {"png", "jpeg"}
	choose from list formatList
	return result
	end tell
EOF

ffotmat=$(osascript -e "$applescriptCode1")

idx=0

for f in "$@";do
	sips -s format $ffotmat --out "${f%.*}.$ffotmat" "$f"
	let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 修改了 $idx 个文件)\""