#!/bin/sh
#
# LaunchBar Action Script
#

for ARG in "$@"; do
		open -n "$ARG" -a "/Applications/calibre.app/Contents/ebook-viewer.app"
done
