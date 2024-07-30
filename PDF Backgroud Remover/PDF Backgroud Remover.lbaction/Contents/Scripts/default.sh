#!/bin/bash
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

for f in "$@"; do
	full_name=${f%.*}
	extension=${f##*.}
	newFile=${full_name}_rmbg.$extension
	gs -o "$newFile" -sDEVICE=pdfwrite -dFILTERVECTOR -dFILTERIMAGE "$f"
done && afplay "/System/Library/Sounds/Submarine.aiff"