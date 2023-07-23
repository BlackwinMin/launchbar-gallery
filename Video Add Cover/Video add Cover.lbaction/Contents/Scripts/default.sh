# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

for f in "$@";do

if [[ $f == *.jpg ]] || [[ $f == *.JPG ]] || [[ $f == *.jpeg ]] || [[ $f == *.JPEG ]]; then
        imageFile="$f"
elif [[ $f == *.mp4 ]]; then
        videoFile="$f"
fi

ffmpeg -i "$videoFile" -i "$imageFile" -map 0 -map 1 -c copy -disposition:v:1 attached_pic "${imageFile%.*}-2.mp4"

#    ffmpeg -i "$f" -map 0:v -map -0:V -c copy "$newFile"
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"Create Cover for ${imageFile%.*}\" with title \"Video to Cover\""