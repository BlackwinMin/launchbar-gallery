# LaunchBar Action Script
#

echo "$# arguments passed"

PATH=$PATH:/usr/local/bin/

idx=0

for f in "$@";do
    full_name=${f%.*}
    extension=${f##*.}
    newFile=${full_name}_new.$extension
    convert "$f" \( +clone -background black -shadow 50x10+0+10 \) +swap -background none -layers merge +repage  "$newFile"
    let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 修改了 $idx 个文件)\""