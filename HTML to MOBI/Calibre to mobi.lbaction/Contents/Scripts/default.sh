# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

echo "$# arguments passed"

idx=0

for f in "$@";do
	ebook-convert "$f" "${f%.*}.mobi"
	let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"Converted $idx books\" with title \"Calibre to mobi\""