#!/bin/bash

# check if argument exists
if [ ! $# -eq 2 ]; then
    echo "Usage: ./sbs.sh <csv-file> <search-file>"
    exit 1
fi

echo -n "Loading site data ... "

#exclude any comment lines from the csv
if [ -f $1 ] && DATA=$(awk '!/^[#]/' $1); then
    echo "Success!"
else
    echo "Failed to load $1"
    exit 1
fi

echo -n "Scanning file $2 ... "

#check if file to scan exists
if ! [ -f $2 ]; then
    echo "Failed to load $2"
    exit 1
fi


#read every line of the data by field
while IFS=, read -r Id FldDateAdded URL URLStatus LastOnline Threat Tags URLHausLink Reporter; do
    #check file the bad URL
    if grep -q "$URL" "$2"; then
        echo "Malicious URL detected!"
        echo "MALICIOUSURL: $URL"
        exit 0
    fi
done <<< "$DATA"

echo "No malicious URL detected"
exit 0 
