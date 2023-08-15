#!/bin/sh
#
# LaunchBar Action Script
#
PATH=$PATH:/usr/local/bin/;
echo "$# arguments passed"
idx=0

for ARG in "$@"; do
# 导入书籍信息到Calibre
ff=`basename "$ARG"`
bookID=$(calibredb add --empty --title "$ff" | egrep -o '\d+')
# 创建alias替身文件
osascript <<EOF
set fFolder to POSIX file "/Users/Min/KM" as aliasset fFile to POSIX file "$ARG" as alias
set fUUID to "cb" & ($bookID as text)tell application "Finder"    make new alias file to fFile at fFolder with properties {name:fUUID}end tell
EOF
# 链接到alias替身文件
bookUUID=file:///Users/Min/KM/cb$bookID
calibredb set_custom uuid $bookID "<p><a href=\"$bookUUID\">External</a></p>"
let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"Imported $idx books\" with title \"Calibre Importer UUID\""