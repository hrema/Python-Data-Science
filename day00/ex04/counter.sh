#!/bin/sh

cp ../ex03/hh_position.csv .

cat hh_position.csv | tail -n +2 | cut -d '"' -f 6 | egrep -v "-" | sort | uniq -c > tmp_name_vacancies

IFS=$'\n'
for entry in $(cat tmp_name_vacancies)
do
	count=0
	IFS=' '
	for value in $entry
	do
		if [ $count -eq 0 ]
		then
			n=$value
		else
			name=$value
		fi
		count=1
	done
	echo "\"$name\",\"$n\"" >> hh_uniq_positions_tmp
done

echo '"name","count"' > hh_uniq_positions.csv
cat hh_uniq_positions_tmp | sort -r -t"," -k2 >> hh_uniq_positions.csv

rm -rf tmp_name_vacancies
rm -rf hh_position.csv
rm -rf hh_uniq_positions_tmp