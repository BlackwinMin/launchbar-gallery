#!/bin/sh
#
# LaunchBar Action Script
#

cd ~/Desktop

idx=0

for ARG in "$@"; do
    #获取源文件的文件名
    basename=${ARG##*/}
    only_name=${basename%.*}
    exported_file=`/Applications/Sketch.app/Contents/Resources/sketchtool/bin/sketchtool export artboards "$ARG" --formats="png"`
    exported_file_path=/Users/apple/Desktop/`echo $exported_file | sed 's/Exported //'`
    #用源文件名来重命名导出的文件
    mv "$exported_file_path" "/Users/apple/Desktop/$only_name.png"
    let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff"

osascript -e "display notification \"$(echo 导出了 $idx 个文件)\""