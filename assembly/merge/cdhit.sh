#! /bin/bash
filename=$1
scriptpath=`dirname $0`

BASE=`basename $filename`

module load bioinformatics-MODULES
module load CDHIT/4.5.6

cd-hit-est -i $BASE -o $BASE.cdhit.out -c .99 -M 9800 -T 8 