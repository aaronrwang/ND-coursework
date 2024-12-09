#!/bin/bash

# check if argument exists
if [ ! $# -eq 1 ]; then
    echo "Usage: ./ae.sh <file>"
    exit 1
fi

# create archive
if [ -d "archive" ]; then
    echo "archive directory already present - no need to create"
else
    echo "archive directory is not present .. creating!"
    mkdir archive
fi

#check file type and do appropriate unzip into archive
if [[ $1 =~ \.zip$ ]]; then
    echo "Extracting a zip file via unzip"
    unzip $1 -d archive > /dev/null 2>&1
elif [[ $1 =~ \.tar$ || $1 =~ \.tar.gz$ ]]; then
    echo "Extracting a tar file"
    tar -xf $1 -C archive > /dev/null 2>&1
elif [[ $1 =~ \.bz2$ ]]; then
    echo "Extracting a bz2 file"
    bunzip2 -c $1 > archive/$(basename $1 .bz2) > /dev/null 2>&1
else
    echo "$1 is neither a ZIP nor a TAR file"
fi

exit 0