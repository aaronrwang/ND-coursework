#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <toscan_path>"
    exit 1
fi

TOSCAN=$1

sh test/feeddirectory.sh ./test/clean_archives $TOSCAN