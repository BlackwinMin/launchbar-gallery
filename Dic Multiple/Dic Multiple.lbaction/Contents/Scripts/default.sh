#!/bin/sh
#
# LaunchBar Action Script
#

for keystr in `echo $@ | sed 's/ / /g'`
do

read -r -d '' applescriptCode1 <<'EOF'
tell application "System Events" to tell process "Dictionary"
EOF
osascript -e "$applescriptCode1"

open dict://$keystr
done