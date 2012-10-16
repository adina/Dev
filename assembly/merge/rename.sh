#! /bin/bash
filename=$1
scriptpath=`dirname $0`

BASE=`basename $filename`

python ~/scripts/merge-assemblies/rename-for-minimus.py $BASE > $BASE.minimus.200

rm report*