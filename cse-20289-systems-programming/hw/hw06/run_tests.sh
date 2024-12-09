#!/bin/bash

current_time=$(date +"%Y-%m-%d_%H-%M")
log_file="${current_time}-UnitTest.log"

echo "Logging output to: $log_file"

# Run Python unit tests and capture stdout and stderr
python3 -m unittest discover -v > "$log_file" 2>&1


if grep -q "OK" "$log_file"; then
    echo "All unit tests passed."
else
    echo "Unittests not passed. Here is the log:"
    cat "$log_file"
fi