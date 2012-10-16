#! /bin/bash
filename=$1
scriptpath=`dirname $0`

BASE=`basename $filename`

cd-hit-est -i $BASE -o $BASE.cdhit.out -c .99 -M 9800 -T 8 