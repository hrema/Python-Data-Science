#!/bin/bash

cat /Users/hrema/Desktop/DS/day00/ex00/hh.json | jq -f -r filter.jq > hh.csv
