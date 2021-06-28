#!/bin/sh

cat ../ex01/hh.csv | head -n 1 > hh_sorted.csv
cat ../ex01/hh.csv | tail -n +2 | sort -t"," -k2 -k1 >> hh_sorted.csv
