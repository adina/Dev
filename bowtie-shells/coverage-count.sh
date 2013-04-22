PREFIX=$1
SEQS=${*:2}
K=20
HASHBITS_SIZE=5e9
N_TABLES=4

python /mnt/data1/khmer/scripts/load-into-counting.py $PREFIX.ht $SEQS -N $N_TABLES -k $K -x $HASHBITS_SIZE 

#python /mnt/data1/khmer-additions/calc-median-coverage.py $PREFIX.ht $PREFIX-contigs.renamed.fa