#!/bin/sh
lineCount=0
numFile=0
for dir in $(ls -d */); do
    cd $dir
    numFile=$((numFile + $(ls | wc -l | sed -e 's/^[ \t]*//')))
    for file in $(ls); do
        line=$(cat $file | wc -l | sed -e 's/^[ \t]*//')
        lineCount=$((lineCount + line))
    done
    cd ..
done

echo "lines: $lineCount"
echo "files: $numFile"
