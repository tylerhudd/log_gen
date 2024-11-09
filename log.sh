#!/bin/bash

# Check if a log type is provided
if [ -z "$1" ]; then
    echo "Please specify the log type. For example, enter:"
    echo "  ./log.sh daily"
    echo "  ./log.sh sim"
    exit 1
fi

# Change directory to the location of this script
cd "$(dirname "$0")/log" || exit

# Call the Python script with the first log type argument
python3 log.py "$1"

# Check for errors
if [ $? -ne 0 ]; then
    echo "Failed to create log file for type: $1"
else
    echo "Log file created successfully for type: $1"
fi
