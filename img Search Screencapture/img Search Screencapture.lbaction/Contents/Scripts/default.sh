# LaunchBar Action Script
#
# 作者：Minja, dofy
#

screencapture -i ~/googleimagesearch.png
#var=$(curl -F smfile=@"/Users/apple/googleimagesearch.png" https://sm.ms/api/v2/upload | grep -o -E 'https:\\/\\/i\.loli\.net\\.*\.png|https:\\/\\/i\.loli\.net\\.*\.jpg|https:\\/\\/i\.loli\.net\\.*\.jpeg' | sed 's/\\//g')
var=$(curl -F smfile=@"/Users/min/googleimagesearch.png" https://sm.ms/api/v2/upload | grep -o -E '"https:\\/\\/s2\.loli\.net\\.*\.(png|jpg|jpeg)"' | sed 's/\\//g' | sed 's/"//g')
var2=https://images.google.com/searchbyimage?image_url=$var
open -a Safari $var2
rm ~/googleimagesearch.png