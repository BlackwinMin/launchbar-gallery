#!/bin/bash
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

for f in "$@"; do
	full_name=${f%.*}
	extension=${f##*.}
	newFile=${full_name}_rmwm.$extension
	gs -o "$newFile" -sDEVICE=pdfwrite -dFILTERVECTOR -dFILTERTEXT "$f"
done && afplay "/System/Library/Sounds/Submarine.aiff"