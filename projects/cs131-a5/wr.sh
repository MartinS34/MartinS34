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
    weighted_rating[$2] += $4 * $6;
    useful_count[$2] += $6;
}
END {
    for (drug in weighted_rating) {
        if (review_count[drug] >= min_reviews) {
            weighted_avg = weighted_rating[drug] / useful_count[drug];
            print drug, weighted_avg;
        }
    }
}
' $input_file | sort -k2,2nr | awk 'BEGIN { OFS="\t"; print "drugName", "weighted_average_rating"; } { print $0; }'


