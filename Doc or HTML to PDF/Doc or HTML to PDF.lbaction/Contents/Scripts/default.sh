#!/bin/sh
#
# LaunchBar Action Script
#

for f in "$@"; do
    filePath=`echo ${f%.*}`
    fileType=`echo ${f##*.} | tr '[A-Z]' '[a-z]'`
    if [ "$fileType" == "html" ];then
        cupsfilter "$f" > "$filePath.pdf"
    elif [ "$fileType" == "docx" ]||[ "$fileType" == "rtf" ];then
        textutil -convert html -output "$filePath.html" "$f"
        cupsfilter "$filePath.html" > "$filePath.pdf"
        rm "$filePath.html" >/dev/null
    else
        osascript -e "display notification \"$(echo $fileType 格式不支持)\""
    fi
done
