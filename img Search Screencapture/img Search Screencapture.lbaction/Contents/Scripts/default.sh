# LaunchBar Action Script
#
# 作者：Minja, dofy
#

screencapture -i ~/googleimagesearch.png
#   从 sm.ms API 切换到 Google API
#var=$(curl -F smfile=@"/Users/min/googleimagesearch.png" https://sm.ms/api/v2/upload | grep -o -E '"https:\\/\\/s2\.loli\.net\\.*\.(png|jpg|jpeg)"' | sed 's/\\//g' | sed 's/"//g')
#var2=https://images.google.com/searchbyimage?image_url=$var
#open -a Safari $var2
var=$(curl -F encoded_image=@"/Users/min/googleimagesearch.png" https://www.google.com/searchbyimage/upload | grep -o -E '"https:.*"' | sed 's/"//g')
echo "$var"
open -a Safari $var
rm ~/googleimagesearch.png