#! /bin/bash
filename=$1
scriptpath=`dirname $0`

BASE=`basename $filename`

python rename-for-minimus.py $BASE > $BASE.minimus.200

rm report*