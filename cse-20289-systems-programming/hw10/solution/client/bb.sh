#!/bin/bash

source .config

if [[ "$1" == '-query' ]]; then
    #args should be -query, filter string, year, month, day, and hour
    echo "$#"
    if [[ "$#" -ne 6 ]]; then
        echo "Usage: $0 -query <filter> <year> <month> <day> <hour>"
        exit 1
    fi
    
    FILTER="$2"
    YEAR="$3"
    MONTH="$4"
    DAY="$5"
    HOUR="$6"
    MSG="$YEAR-$MONTH-$DAY, $HOUR, $FILTER"
else
    #args should be year, month, day, and hour
    if [[ "$#" -ne 4 ]]; then
        echo "Usage: $0 <year> <month> <day> <hour>"
        exit 1
    fi

    YEAR="$1"
    MONTH="$2"
    DAY="$3"
    HOUR="$4"
    MSG="$YEAR-$MONTH-$DAY, $HOUR, *"
fi

./"$EXE" "$HOST" "$PORT" <<EOF
count, $MSG
mean, $MSG
median, $MSG
min, $MSG
max, $MSG
stddev, $MSG
list, $MSG
more
more
exit
EOF

exit 0