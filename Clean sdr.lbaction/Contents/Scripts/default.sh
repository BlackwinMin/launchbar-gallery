#!/bin/sh
#
# LaunchBar Action Script
#

dir=$(dirname "$ARG")

cd $dir

for ARG in "$@"; do
    mobi=$(echo "$ARG" | sed 's/sdr/mobi/g')
    txt=$(echo "$ARG" | sed 's/sdr/txt/g')
    pdf=$(echo "$ARG" | sed 's/sdr/pdf/g')
    kfx=$(echo "$ARG" | sed 's/sdr/kfx/g')
    azw=$(echo "$ARG" | sed 's/sdr/azw3/g')

    if [[ "$ARG" =~ "sdr" ]] && [[ ! -e "$mobi" ]] && [[ ! -e "$txt" ]] && [[ ! -e "$pdf" ]] && [[ ! -e "$kfx" ]] && [[ ! -e "$azw3" ]]; then
        rm -rf "$ARG"
    fi
done && afplay "/System/Library/Sounds/Submarine.aiff"