# LaunchBar Action Script

PATH=$PATH:/usr/local/bin/

for ARG in "$@"; do
	ooutput="$ARG.zip"
	7z a -tzip -r "$ooutput" "$ARG"
	zip -q -d "$ooutput" *__MACOSX* || true
	zip -q -d "$ooutput" \*.DS_Store || true
done && afplay "/System/Library/Sounds/Submarine.aiff"