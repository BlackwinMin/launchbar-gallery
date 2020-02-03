#!/bin/sh
#
# LaunchBar Action Script
#
# 因为太懒所以把纯色背景路径写死了
#

currentWallpaper=`osascript -e 'tell app "finder" to get posix path of (get desktop picture as alias)'`

#echo $currentWallpaper

if [[ "$currentWallpaper" =~ "Solid Color Blue Violet" ]]; then

newWallpaper=`cat haha.txt`
#echo $newWallpaper
osascript <<EOF
tell application "System Events"
    tell current desktop
        set picture to "$newWallpaper"
    end tell
end tell
EOF
defaults write com.apple.finder CreateDesktop -bool TRUE; killall Finder

else

echo $currentWallpaper > haha.txt
osascript <<EOF
tell application "System Events"
    tell current desktop
        set picture to "/Users/apple/Library/Application Support/LaunchBar/Actions/Desktop Hide&Show.lbaction/Contents/Scripts/Solid Color Blue Violet.png"
    end tell
end tell
EOF
defaults write com.apple.finder CreateDesktop -bool FALSE; killall Finder

fi