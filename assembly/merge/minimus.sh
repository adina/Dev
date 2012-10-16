#! /bin/bash
filename=$1
scriptpath=`dirname $0`

BASE=`basename $filename`

module load bioinformatics-MODULES
module load expat BLAT Qt MUMmer
module load AMOS/3.1.0a

toAmos -s $BASE -o $BASE.afg 
minimus2 $BASE