# LaunchBar Action Script

PATH=$PATH:/usr/local/bin/

ARG="$1"
ddate=`date +%Y-%m-%d-%H%M%S`
ooutput="${ARG%/*}/Archive-$ddate.zip"

read -r -d '' applescriptCode1 <<'EOF'
	set f to text returned of (display dialog "Enter Password if you like" default answer "")
	return f
EOF

PASSWORD=$(osascript -e "$applescriptCode1")

if [ -z "$PASSWORD" ]; then
	7z a -tzip -r "$ooutput" "$@" && afplay "/System/Library/Sounds/Submarine.aiff"
else
	7z a -tzip -r "$ooutput" "$@" -p"$PASSWORD" && afplay "/System/Library/Sounds/Submarine.aiff"
fi

zip -q -d "$ooutput" *__MACOSX* || true
zip -q -d "$ooutput" \*.DS_Store || true