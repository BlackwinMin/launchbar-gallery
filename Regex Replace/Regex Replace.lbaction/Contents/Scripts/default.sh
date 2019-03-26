#!/bin/bash
#
# LaunchBar Action Script
#

read -r -d '' applescriptCode1 <<'EOF'
    set reg to text returned of (display dialog "请输入要替换的文本" default answer "哈哈")
    return reg
EOF

read -r -d '' applescriptCode2 <<'EOF'
    set pattern to text returned of (display dialog "请输入替换后的文本" default answer "呵呵")
    return pattern
EOF

reg=$(osascript -e "$applescriptCode1")

pattern=$(osascript -e "$applescriptCode2")

echo $@ | sed 's/'$reg'/'$pattern'/g' | pbcopy

osascript -e 'tell application "System Events" to key code 9 using command down'