#!/bin/sh

awk 'FNR==NR||FNR>1' [0-9]* > hh_position.csv
rm -rf [0-9]*