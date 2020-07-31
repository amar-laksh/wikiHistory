#!/bin/bash
# File              : process.sh
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 30.07.2020
# Last Modified Date: 30.07.2020
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>

files=$(ls *.csv)
mkdir -p data

header="date,year,person,desc"
for file in $files; do
	cat $file | sed 's/\s*–\s*/,/g' | sed 's/\s*,\s*/,/g' > data/$file
	noOfColumns=$(sed 's/[^,]//g' data/$file | wc -L)
	for i in $(seq $(expr $noOfColumns + 1)); do
		header="$header,NA"
	done
	sed -i "1s;^;$header\n;" data/$file
done

