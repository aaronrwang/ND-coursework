#!/bin/bash

# This script copies all files from a given directory to the 'toscan' directory

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <archive-path> <toscan_path>"
    exit 1
fi

SOURCE_DIR=$1
TARGET_DIR=$2

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Directory $SOURCE_DIR does not exist."
    exit 1
fi

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Directory $TARGET_DIR does not exist."
    exit 1
fi

# Loop through each file in the source directory and copy it to the toscan directory
for file in "$SOURCE_DIR"/*; do
    if [ -f "$file" ]; then
        echo "Copying $file to $TARGET_DIR"
        cp "$file" "$TARGET_DIR/"
        sleep 2  # Sleep for 2 seconds between copies to simulate delays
    fi
done

echo "Finished copying files from $SOURCE_DIR to $TARGET_DIR."

exit 0