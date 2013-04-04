#! /bin/bash


SEQS=$1
SCRIPTPATH=`dirname $0`

BASENAME=`basename $SEQS .gz`
BASENAME=`basename $BASENAME .fa`
BASENAME=`basename $BASENAME .fasta`
BASENAME=`basename $BASENAME .fq`

K=20
HASHBITS_SIZE=1e9
N_TABLES=4
SUBSET_SIZE=1e5
KEEP_SUBSETS=    # --keep-subsets turns on
OUTPUT_GROUPS=-n # -n prevents groups from being output

$SCRIPTPATH/load-graph.py -k $K -x $HASHBITS_SIZE -N $N_TABLES $BASENAME $SEQS
$SCRIPTPATH/partition-graph.py --subset-size $SUBSET_SIZE $BASENAME
$SCRIPTPATH/merge-partitions.py -k $K $BASENAME
$SCRIPTPATH/annotate-partitions.py -k $K $BASENAME $SEQS
$SCRIPTPATH/extract-partitions.py $BASENAME `basename ${SEQS}`.part
