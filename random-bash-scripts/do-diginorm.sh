#! /bin/bash

PREFIX=$1
SEQS=${*:2}
SCRIPTPATH=/mnt/data1/khmer/scripts
SCRIPTPATH2=/mnt/data1/khmer/sandbox

K=20
HASHBITS_SIZE=1e9
N_TABLES=4
C=20

#echo python $SCRIPTPATH/normalize-by-median.py -k $K -C $C -N $N_TABLES -x $HASHBITS_SIZE -s $PREFIX.diginorm1.kh -R $PREFIX.diginorm1.report $SEQS

#python $SCRIPTPATH/normalize-by-median.py -k $K -C $C -N $N_TABLES -x $HASHBITS_SIZE -s $PREFIX.diginorm1.kh -R $PREFIX.diginorm1.report $SEQS

echo python $SCRIPTPATH2/filter-below-abund.py Sample_$PREFIX/$PREFIX.diginorm1.kh $SEQS

python $SCRIPTPATH2/filter-below-abund.py Sample_$PREFIX/$PREFIX.diginorm1.kh $SEQS


# $SCRIPTPATH/partition-graph.py --subset-size $SUBSET_SIZE $BASENAME
# $SCRIPTPATH/merge-partitions.py -k $K $BASENAME
# $SCRIPTPATH/annotate-partitions.py -k $K $BASENAME $SEQS
# $SCRIPTPATH/extract-partitions.py $BASENAME `basename ${SEQS}`.part
