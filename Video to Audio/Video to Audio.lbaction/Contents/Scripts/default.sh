# LaunchBar Action Script
#

echo "$# arguments passed"

PATH=$PATH:/usr/local/bin/

idx=0

for f in "$@";do
    newFile=${f%.*}.mp3
    ffmpeg -i "$f" -b:a 128k "$newFile"
    let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 生成了 $idx 段音频)\""