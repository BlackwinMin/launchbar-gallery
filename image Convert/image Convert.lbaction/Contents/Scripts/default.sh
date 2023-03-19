#!/bin/sh
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

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

fformat=$(osascript -e "$applescriptCode1")

idx=0

for f in "$@";do
	if [[ "${f##*.}" =~ "pdf" ]]; then
		convert -density 300 "$f"[0] "${f%.*}.$fformat"
	else
		sips -s format $fformat --out "${f%.*}.$fformat" "$f"
	fi
	let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"Converted $idx images\" with title \"image Convert\""