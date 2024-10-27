#!/bin/bash

# Input and output file names
input_file="./../data/参比制剂.json"
output_file="./../data/参比制剂.csv"

# Extract keys for the header
header=$(jq -r '.[0] | keys | @csv' "$input_file")

# Extract values for each record and convert to CSV format
rows=$(jq -r '.[] | [.idCode, .ypmc, .jx, .gg, .cbzj, .pzwh, .scpzrq, .ssxkzcyr, .sccs] | @csv' "$input_file")

# Write header and rows to output file
echo "$header" > "$output_file"
echo "$rows" >> "$output_file"

echo "Data has been written to $output_file"
