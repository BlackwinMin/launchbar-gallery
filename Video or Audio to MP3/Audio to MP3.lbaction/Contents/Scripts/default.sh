# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

idx=0

for f in "$@";do
    newFile=${f%.*}.mp3
#   ffmpeg -i "$f" -ab 320k -map_metadata 0 -id3v2_version 3 "$f".mp3
    ffmpeg -i "$f" -ab 320k -map_metadata 0 -id3v2_version 3 "$newFile"
    let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"Create $idx files\" with title \"Audio to MP3\""