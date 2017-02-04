#!/bin/bash

for file in *
	do uncompyle2 -o $file"_done" $file
	outputfile=$(echo $file"_done" | sed 's/pyc\_done/py/')
	mv $file"_done" $outputfile 
	
done
rm *_failed

#echo -e "\n\n\n\n\n\n\n\n...hit enter"
#read Ucase
rm *.pyc
