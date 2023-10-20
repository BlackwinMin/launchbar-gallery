#!/bin/sh
#
# LaunchBar Action Script
#


if [[ "$@" =~ "x-devonthink-item" ]]; then
	open "$@"
else
	open "$@" -a "/Applications/calibre.app/Contents/ebook-viewer.app"
fi