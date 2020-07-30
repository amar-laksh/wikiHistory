#!/bin/bash
# File              : process.sh
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 30.07.2020
# Last Modified Date: 30.07.2020
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>

files=$(ls *.csv)
columns="date,year,person,desc,NA,NA,NA,NA,NA,NA,NA,NA"
mkdir -p data
for file in $files; do
	cat $file | sed 's/\s*–\s*/,/g' | sed 's/\s*,\s*/,/g' > data/$file
	sed -i "1s;^;$columns\n;" data/$file
done
