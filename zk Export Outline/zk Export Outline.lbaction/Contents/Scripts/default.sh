# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/

for f in "$@";do
    folderA="/Users/Min/Library/Mobile Documents/iCloud~md~obsidian/Documents"
	folderB="/Users/Min/Downloads/待转给同事/"
	not_found_file="$folderB/not_found.txt"	
	> "$not_found_file"
	
	extracted_texts=$(sed -n 's/.*\[\[\(.*\)\]\].*/\1/p' "$f")
	
	echo "$extracted_texts" | while IFS= read -r text; do
	  found_files=$(find "$folderA" -type f -name "$text*")  
	  if [ -z "$found_files" ]; then
		echo "未找到文件：$text" >> "$not_found_file"
		echo "未找到文件：$text，记录到 $not_found_file"
	  else
		echo "$found_files" | while IFS= read -r file; do
		  relative_path="${file#$folderA/}"
		  destination="$folderB/$relative_path"
		  mkdir -p "$(dirname "$destination")"
		  cp "$file" "$destination"
		done
	  fi
	done
done