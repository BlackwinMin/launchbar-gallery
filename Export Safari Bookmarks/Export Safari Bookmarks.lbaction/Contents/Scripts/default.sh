#!/bin/sh
#
# LaunchBar Action Script
#

#if [ -z "$@" ]; then
#    PATH=$PATH:/usr/local/bin/;python3 "./export.py" "$@"
#else
#    PATH=$PATH:/usr/local/bin/;python3 "./export.py"
#fi
if [ -z "$@" ]; then
    PATH=$PATH:/usr/local/bin/;python3 "./export.py"
else
    PATH=$PATH:/usr/local/bin/;python3 "./export.py" "$@"
fi