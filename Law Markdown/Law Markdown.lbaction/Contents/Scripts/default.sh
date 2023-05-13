#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"

export LANG="en_US.UTF-8"
PATH=$PATH:/usr/local/bin/

for ARG in "$@"; do    
    cat "$ARG" | tr -s "\n"\
    | sed -E -e "s/(^第.{0,6}[一二三四五六七八九十百千]条)/**\1**/g" \
    -e "s/(^第.{1,3}编.*|^附件.*)/# \1/g" \
    -e "s/(^第.{1,3}章.*|^附则)/## \1/g" \
    -e "s/(^.{0,2}[一二三四五六七八九十百千]、.*)/## \1/g" \
    -e "1 s/.*/# &/" \
    -e "s/(^第.{1,3}节.*)/### \1/g" "$ARG" \
    | tr -s "\n"\ | perl -p -e 's/\n/\n\n/' | pbcopy
#   | tr -s "\n"\ | perl -p -e 's/\n/\n\n/' > "$ARG.md"
#   sed -i "" "1 s/.*/# &/" "$ARG.md"
done
