#!/bin/sh
#
# LaunchBar Action Script
#

cat ./suggetList.txt | while read line;do
	if [[ $line =~ $@ ]] && [[ $@ != "" ]]; then
		echo $line
	elif [ -z "$@" ]; then
		echo $line
	fi
done