#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <file-to-scan>"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "File $FILE not found!"
    
    exit 1
fi


# Print message indicating scanning
echo "Scanning for sensitive information"
echo "File to scan: $FILE"

#utilization of \b to indicate a separated word 
if grep -q "\*SENSITIVE\*" "$FILE"; then
    echo "SENSITIVE, MARKED SENSITIVE"
#ssn
elif grep -qE "\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b" "$FILE"; then
    echo "SENSITIVE, SSN"
#ndid
elif grep -qE "\b9[0-9]{8}\b" "$FILE"; then
    echo "SENSITIVE, STUDENTID"
else
    echo "CLEAN"
fi

exit 0