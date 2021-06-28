#!/bin/bash

cp /Users/hrema/Desktop/DS/day00/ex02/hh_sorted.csv hh_position.csv

cat hh_position.csv | egrep -i "junior|middle|senior" | cut -d '"' -f 6 > tmp_good_vacantions

j=.*junior.*

IFS=$'\n'
for entry in $(cat tmp_good_vacantions)
do
	IFS=' '
	for value in $entry
	do
		lower_value=$(echo "$value" | tr '[:upper:]' '[:lower:]')
		if [[ $lower_value =~ .*junior|middle|senior.* ]]
		then
			if [ ${value:0:1} = '(' ]
			then
				value=$(echo ${value:1})
			fi
			length=${#value}
			length=$(($length-1))
			if [ "${value:$length:1}" = ")" ]
			then
				value=$(echo ${value:0:$length})
			fi
			n=$(cat hh_position.csv | grep -n -i "$entry" | cut -d ":" -f1 | head -n 1)
			sed -i '' "$n s#$entry#$value#" hh_position.csv
		fi
	done
done
rm -rf tmp_good_vacantions

cat hh_position.csv | tail -n 20 | egrep -v "Junior|Middle|Senior" | cut -d '"' -f 6 > tmp_bad_vacantions
while read line
do
	n=$(cat hh_position.csv | grep -n "$line" | cut -d ":" -f1 | head -n 1)
	sed -i '' "$n s#$line#-#1" hh_position.csv
done < tmp_bad_vacantions
rm -rf tmp_bad_vacantions
