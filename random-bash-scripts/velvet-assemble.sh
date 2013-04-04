#! /bin/bash
filename=$1
K=$2

BASE=`basename $filename`

velveth $BASE.ass.$K $K -fasta -short ${BASE} && \
velvetg $BASE.ass.$K -read_trkg yes -exp_cov auto -cov_cutoff auto -scaffolding no

rm ${BASE}.ass.$K/{Graph2,LastGraph,PreGraph,Roadmaps,Sequences}
