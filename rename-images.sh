#! /bin/bash

if [ -z "$1" ];then
	echo "No argument supplied"
	exit 1
else
	BASEFILENAME=$1
	ls ./tmp/*.jpg| awk -v FILE="$BASEFILENAME" 'BEGIN{ a=0 }{ printf "mv %s ./tmp/"FILE"_%04d.jpg\n", $0, a++ }' | bash	
fi

#ls ./tmp/*.jpg| awk -v FILE="$BASEFILENAME" 'BEGIN{ a=0 }{ printf "mv %s ./tmp/FILE_%04d.jpg\n", $0, a++ }'

