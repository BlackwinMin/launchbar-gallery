# LaunchBar Action Script
#


PATH=$PATH:/usr/local/bin/

ARG="$1"
ddate=`date +%Y-%m-%d-%H%M%S`
ooutput="${ARG%/*}/concact-$ddate.png"

#osascript -e "display notification \"$(echo $ooutput)\""
#osascript -e "display notification \"$(echo $ARG)\""

#convert "$@" -background none +append "$ooutput" && afplay "/System/Library/Sounds/Submarine.aiff"
convert "$@" -background none +append "$ooutput" && afplay "/System/Library/Sounds/Submarine.aiff"