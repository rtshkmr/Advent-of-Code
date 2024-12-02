#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <year> <day> <session_cookie> <output_directory>"
    exit 1
fi

YEAR=$1
DAY=$2
SESSION_COOKIE=$3
OUTPUT_DIR=$4

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Download the input file for the specified year and day
curl "https://adventofcode.com/$YEAR/day/$DAY/input" \
  --cookie "session=$SESSION_COOKIE" \
  -o "$OUTPUT_DIR/${YEAR}_day${DAY}_input.txt"

if [ $? -eq 0 ]; then
    echo "Input for Day $DAY of Year $YEAR downloaded successfully to $OUTPUT_DIR."
else
    echo "Failed to download input for Day $DAY of Year $YEAR."
fi
