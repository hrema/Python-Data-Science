#!/bin/sh

s="$(head -n 1 hh_position.csv)"
# echo $s | cat -e
cat hh_position.csv | tail -n +2 | awk -F '"' '{ split ($4,array,"T"); print $0 >> array[1] }'
for file in [0-9]*
do
	gsed -i "1 s#^#$s\n#" $file
done
# rm -rf [0-9]*