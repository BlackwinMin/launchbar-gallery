#!/bin/sh
#
# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

read -r -d '' applescriptCode1 <<EOF
    tell application "System Events"
        set activeApp to name of first application process whose frontmost is true
        activate
        set file_wid_display to "$file_wid" as string
        set widList to {"原始尺寸", "3/4", "2/3", "1/2", "1/3","other"}
        choose from list widList with title "选择输出尺寸" default items "原始尺寸"
        if result contains "原始尺寸" then
            set widChoose to "$file_wid" as number
        else if result contains "other" then
            set widChoose to text returned of (display dialog "请输入自定义尺寸" default answer "0")
        else
            set widChoose to result
        end if
    end tell
    return widChoose
EOF

idx=0

for f in "$@";do
    
    # 选择预设分辨率或自定义分辨率
    file_wid=$(ffmpeg -i "$f" 2>&1 | grep -E -o '\d{3,}x\d{3,}' | grep -E -o '^\d{3,}')
    
    widChoose=$(osascript -e "$applescriptCode1")
    #echo $file_wid
    #echo $widChoose
    if [[ "$widChoose" = "$file_wid" ]];then
        let widOutput=$widChoose
    elif [[ "$widChoose" =~ "/" ]];then
        let widOutput=$file_wid*$widChoose
    else
        let widOutput=$widChoose
    fi
    #echo $widOutput
    
    full_name=${f%.*}
    extension=${f##*.}
    newFile=${full_name}_new.mp4
    temp1=$(echo $extension | tr [a-z] [A-Z])
    if [[ "$temp1"x = "MP4"x ]] || [[ "$temp1"x = "MOV"x ]]; then
        ffmpeg -i "$f" -vf scale="$widOutput:-2" -b:v 600k -f mp4 "$newFile"
        let idx=$idx+1
    fi
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "display notification \"$(echo 修改了 $idx 个文件)\""