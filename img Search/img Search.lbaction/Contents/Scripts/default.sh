#!/bin/sh
#
# LaunchBar Action Script
#
# 作者：Minja, dofy
#

echo "$# arguments passed"
for ARG in "$@"; do
#    var=$(curl -F smfile=@"$@" https://sm.ms/api/v2/upload | grep -o -E 'https:\\/\\/i\.loli\.net\\.*\.png|https:\\/\\/i\.loli\.net\\.*\.jpg|https:\\/\\/i\.loli\.net\\.*\.jpeg' | sed 's/\\//g')
    var=$(curl -X POST -F smfile=@"$ARG" https://sm.ms/api/v2/upload | grep -o -E '"https:\\/\\/i\.loli\.net\\.*\.(png|jpg|jpeg)"' | sed 's/\\//g' | sed 's/"//g')
    var2=https://images.google.com/searchbyimage?image_url=$var
    open -a Safari $var2
done