#!/bin/bash

# Check if the directory path and filename are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory_path> <filename>"
    exit 1
fi

directory_path=$1
filename="$2.guff"

# Replace colons with hyphens in the filename
filename=${filename//:/-}

# Check if the provided path is a valid directory
if [ ! -d "$directory_path" ]; then
    echo "Error: $directory_path is not a valid directory."
    exit 1
fi

# Initialize variables
largest_file=""
largest_size=0

# Loop through all files in the specified directory
for file in "$directory_path"/*; do
    if [ -f "$file" ]; then
        size=$(stat -c%s "$file")
        if [ $size -gt $largest_size ]; then
            largest_size=$size
            largest_file=$file
        fi
    fi
done

# Check if a largest file was found
if [ -n "$largest_file" ]; then
    echo "The largest file is: $largest_file"
    cp "$largest_file" "./$filename"
    echo "The largest file has been copied to ./$filename."
else
    echo "No files found in the directory."
fi
