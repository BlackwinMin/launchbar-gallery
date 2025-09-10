#!/bin/sh
#
# LaunchBar Action Script
#

for ARG in "$@"; do
		"/Applications/calibre.app/Contents/MacOS/ebook-edit" "$ARG"
done
