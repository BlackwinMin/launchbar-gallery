# LaunchBar Action Script
#
#Credit: https://stackoverflow.com/questions/718314/rounding-corners-of-pictures-with-imagemagick
#

PATH=$PATH:/usr/local/bin/;

inputFilePath=/Users/apple/Desktop/haah.png
outputFilePath=/Users/apple/Desktop/haah-2.png
idx=0

for f in "$@";do
    full_name=${f%.*}
    extension=${f##*.}
    tempFile=${full_name}_temp.$extension
    newFile=${full_name}_new.$extension
    convert "$f" \
        \( +clone  -alpha extract \
            -draw 'fill black polygon 0,0 0,15 15,0 fill white circle 15,15 15,0' \
            \( +clone -flip \) -compose Multiply -composite \
            \( +clone -flop \) -compose Multiply -composite \
        \) -alpha off -compose CopyOpacity -composite "$tempFile"
    convert "$tempFile" \( +clone -background black -shadow 50x10+0+10 \) +swap -background none -layers merge +repage  "$newFile"
    rm "$tempFile"
    let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 修改了 $idx 个文件)\""