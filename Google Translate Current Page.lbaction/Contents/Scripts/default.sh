#!/bin/bash

urlquote()
{
[[ $# = 0 ]]&&echo urlquote string&&return
echo "#coding=utf-8;
import urllib,sys;print urllib.quote('$1');" |python
}

read -r -d '' applescriptCode1 <<'EOF'
    tell application "Safari"
        set ttab to URL of current tab of window 1
    end tell
    return ttab
EOF
ttab=$(osascript -e "$applescriptCode1")

hhead="http://translate.google.com/translate?u="
ttail="&hl=zh-CN&langpair=auto|zh-CN&tbb=1&ie=UTF-8"
tabencoded=`urlquote "$ttab"`

#searchurl=$hhead$tabencoded$ttail
searchurl=$hhead$ttab$ttail

open -a Safari $searchurl