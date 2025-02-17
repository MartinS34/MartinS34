#!/bin/bash
#THIS SCRIPT WAS USED TO FILTER ANXIET MEDS > top5.tsv
# Define the top 5 drugs
top_drugs=("Diazepam" "Valium" "Xanax" "Alprazolam" "Lorazepam")

# Original TSV file
input_file="/Users/martiin/Desktop/a5_ds/FinalDrugDS.tsv"

# New TSV file to create
output_file="/Users/martiin/Desktop/a5_ds/top5.tsv"

# Extract the header
head -n 1 "$input_file" > "$output_file"

# Loop through each drug and append the matching lines to the new file
for drug in "${top_drugs[@]}"; do
  grep -i -F "$drug" "$input_file" >> "$output_file"
done
