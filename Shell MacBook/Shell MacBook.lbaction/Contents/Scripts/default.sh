# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

#调用提示框
read -r -d '' applescriptCode1 <<'EOF'
    set list_1 to {"MacBook", "MacBook Pro", "iMac 5K", "iMac Pro", "ThinkVision T27", "Dell UltraSharp 27"}
    tell application "System Events"
            set activeApp to (name of first application process whose frontmost is true)
            activate
            set shellImage to (choose from list list_1 with title "请选择套壳模板" default items "MacBook") as string
    end tell
    return shellImage
EOF
shellImage=$(osascript -e "$applescriptCode1")

for f in "$@";do
    full_name=${f%.*}
    newFile=${full_name}_shelled.png
    if [ "$shellImage" = "MacBook" ]; then
        composite "-geometry" "+398+121" "$f" "$shellImage".png "$newFile"
    elif [ "$shellImage" = "MacBook Pro" ]; then
        composite "-geometry" "+400+119" "$f" "$shellImage".png "$newFile"
    elif [ "$shellImage" = "iMac 5K" ]; then
        composite "-geometry" "+110+118" "$f" "$shellImage".png "$newFile"
    elif [ "$shellImage" = "iMac Pro" ]; then
        composite "-geometry" "+113+110" "$f" "$shellImage".png "$newFile"
    elif [ "$shellImage" = "ThinkVision T27" ]; then
        composite "-geometry" "+45+43" "$f" "$shellImage".png "$newFile"
    elif [ "$shellImage" = "Dell UltraSharp 27" ]; then
        composite "-geometry" "+30+30" "$f" "$shellImage".png "$newFile"
    fi
done && afplay "/System/Library/Sounds/Submarine.aiff"