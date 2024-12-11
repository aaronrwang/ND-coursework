#!/bin/bash

# check one or three arguments
if [ $# -ne 1 -a $# -ne 3 ]; then
    echo "Usage: $0 <archive-file> (-ad X)"
    exit 1
fi

# if three arguments check arg2 = -ad and third is 1,2,3
if [ $# -eq 3 ]; then
    # Check if the second argument exists and equals '-ad'
    if [ "$2" != "-ad" ]; then
        echo "Error: Second argument must be '-ad'."
        exit 1
    fi

    # Check if the third argument is provided and is one of 1, 2, or 3
    if [[ ! "$3" =~ ^[123]$ ]]; then
        echo "Error: Third argument must be 1, 2, or 3."
        exit 1
    fi
fi

MAX_DEPTH=0
ARCHIVE_FILE="$1"
EXTRACT_DIR="archive"

if [ $# -eq 3 ]; then
    MAX_DEPTH=$3
fi

#if it exists
if [ ! -f "$ARCHIVE_FILE" ]; then
    echo "Error: Archive file $ARCHIVE_FILE does not exist."
    exit 1
fi

echo "Extracting archive: $ARCHIVE_FILE"
sh ae.sh "$ARCHIVE_FILE" > /dev/null 2>&1

# Iterate over each file inside the 'archive' directory
for FILE in $(find "$EXTRACT_DIR" -maxdepth $(($MAX_DEPTH + 2)) -type f); do

    # Checking file for malicious URLs (ingore errors)
    if sh sbs.sh "$FILE" ./badsites/badsite-250.csv  2> /dev/null | grep -q "MALICIOUSURL"; then
        echo "MALICIOUSURL detected in $FILE"
        rm -rf "$EXTRACT_DIR"/*
        exit 0
    fi

    # Checking file for sensitive information (ignore errors)
    if sh sf.sh "$FILE"  2>/dev/null | grep -q "SENSITIVE"; then
        echo "SENSITIVE information detected in $FILE"
        rm -rf "$EXTRACT_DIR"/*
        exit 0
    fi
done

echo "CLEAN"

rm -rf "$EXTRACT_DIR"/*

exit 0