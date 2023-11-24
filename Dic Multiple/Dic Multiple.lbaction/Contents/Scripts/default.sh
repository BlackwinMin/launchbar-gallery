#!/bin/sh
#
# LaunchBar Action Script
#

for keystr in `echo $@ | sed 's/ / /g'`
do

read -r -d '' applescriptCode1 <<'EOF'
tell application "System Events" to tell process "Dictionary"	activate	click menu item "New Window" of menu "File" of menu bar 1	set frontmost to trueend tell	
EOF
osascript -e "$applescriptCode1"

open dict://$keystr
done