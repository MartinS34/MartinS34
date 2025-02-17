#!/bin/bash

input_file="/Users/martiin/Desktop/a5_ds/FinalDrugDS.tsv"

condition="ADHD"  # Specify the condition you want to filter by
min_reviews=25    # Minimum number of reviews

awk -F'\t' -v cond="$condition" -v min_reviews="$min_reviews" '
BEGIN {
    OFS="\t";
}
NR > 1 && $3 == cond {
    review_count[$2]++;
    total_rating[$2] += $4;
}
END {
    for (drug in total_rating) {
        if (review_count[drug] >= min_reviews) {
            mean_rating = total_rating[drug] / review_count[drug];
            print drug, mean_rating;
        }
    }
}
' $input_file | sort -k2,2nr | awk 'BEGIN { OFS="\t"; print "drugName", "mean_rating"; } { print $0; }'

