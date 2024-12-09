
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




# Run the EXE and send the required commands via stdin
./"$EXE" "$HOST" "$PORT" <<EOF | while read -r line; do

count, $MSG
mean, $MSG
median, $MSG
min, $MSG
max, $MSG
stddev, $MSG
list, $MSG
more
more
more
more
exit
EOF

    # Check if the line contains "Received: success" and extract the key-value pair
    if [[ "$line" =~ Received:\ success,\ ([a-zA-Z]+),\ ([^,]+)$ ]]; then
    
        KEY="${BASH_REMATCH[1]}"  # The metric name (e.g., count, mean, etc.)
        VALUES="${BASH_REMATCH[2]}"  # The numeric value (e.g., 213, 228.712, etc.)
        echo Statistic: $KEY '|' Date: "$YEAR-$MONTH-$DAY" '|' Hour: "$HOUR" '|' Value: $VALUES 



    elif [[ "$line" =~ Received:\ ([^,]+),.*mac,\s*([^\s,]+).*test_uuid,\s*([^\s,]+).*interface,\s*([^\s,]+) ]]; then

    
        ITEMSLEFT="${BASH_REMATCH[1]}"
        MAC="${BASH_REMATCH[2]}"
        TEST_UUID="${BASH_REMATCH[3]}"
        INTERFACE="${BASH_REMATCH[4]}"
       
        echo Items Left "$ITEMSLEFT" '|' Mac ID: "$MAC" '|' Test ID: "$TEST_UUID" '|' Interface: $INTERFACE



    fi
    

done

exit 0