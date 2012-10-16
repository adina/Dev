#! /bin/bash
filename=$1
scriptpath=`dirname $0`

BASE=`basename $filename`

toAmos -s $BASE -o $BASE.afg 
minimus2 $BASE