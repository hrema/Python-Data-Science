#!/bin/bash

cat /Users/hrema/Desktop/DS/day00/ex01/hh.csv | head -n 1 > hh_sorted.csv
cat /Users/hrema/Desktop/DS/day00/ex01/hh.csv | tail -n 20 | sort -t"," -k2 -k1 >> hh_sorted.csv
