#!/bin/bash
source .config

# Start the client once with the HOST and PORT
echo "Starting client with host: $HOST, port: $PORT",

# Run ./client only once with host and port as arguments
./"$EXE" "$HOST" "$PORT" <<EOF
count,2024-05-18,*,*
list,2024-05-18,*,interface=eth0;direction=downlink;type=iperf
more
more
min,2024-05-18,*,interface=eth0;direction=downlink
max,2024-05-18,*,interface=eth0;direction=downlink
stddev,2024-05-18,*,interface=eth0;direction=downlink
mean,2024-05-18,*,interface=eth0;direction=downlink
count,2024-05-06,*,interface=eth0;direction=downlink
count,2024-02-16,*,interface=eth0;direction=downlink
count,2024-02-16,*,interface=eth0;direction=downlink;type=speedtest
min,2024-03-23,11,interface=wlan0
exit
EOF

# Check if ./client failed (non-zero exit code)
if [ $? -ne 0 ]; then
    echo "Error running client"
    exit 1
fi

echo "All tests completed."
