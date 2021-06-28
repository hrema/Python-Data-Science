#!/bin/sh

cat ../ex00/hh.json | jq -f -r filter.jq > hh.csv
