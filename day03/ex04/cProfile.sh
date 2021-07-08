#!/bin/sh

script="financial-enhanced"
ticker="FB"
field="Total Revenue"
sort="ncalls"
output_file="profiling-ncalls.txt"

python3 -m cProfile -s $sort -m $script $ticker "$field" > $output_file
