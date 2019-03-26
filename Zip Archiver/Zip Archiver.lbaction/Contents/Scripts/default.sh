# LaunchBar Action Script

PATH=$PATH:/usr/local/bin/

ARG="$1"
ddate=`date +%Y-%m-%d-%H%M%S`
ooutput="${ARG%/*}/Archive-$ddate.zip"

7z a -tzip -r "$ooutput" "$@" && afplay "/System/Library/Sounds/Submarine.aiff"

zip -q -d "$ooutput" *__MACOSX* || true
zip -q -d "$ooutput" \*.DS_Store || true