# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

idx=0

#for f in "$@";do
#done

# 截图保存路径
ddate=`date +%Y-%m-%d-%H%M%S`
output_dir=$(dirname "$1")/seek_$ddate
mkdir -p "$output_dir"
# 获取视频时长
duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1")
# 计算每十六分之一的时间间隔
interval=$(echo "scale=2; $duration / 16" | bc)
# 截取视频缩略图
for i in {0..14}; do
    # 计算时间点
    timestamp=$(echo "$interval * $i" | bc)
    timestamp2=${timestamp%.*}
    hours=$((timestamp2 / 3600))
    remainder=$((timestamp2 % 3600))
    minutes=$((remainder / 60))
    seconds=$((remainder % 60))
    fname="$hours-$minutes-$seconds"
    # 使用 FFmpeg 截取缩略图
    ffmpeg -ss "$timestamp" -i "$1" -frames:v 1 "$output_dir/$fname.jpg" && let idx=$idx+1
done && afplay "/System/Library/Sounds/Submarine.aiff" && osascript -e "tell application \"LaunchBar\" to display in notification center \"Create $idx Thumbnails\" with title \"Video Seek\""