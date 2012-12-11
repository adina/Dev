python multi-rename.py *fa
python multi-cdhit.py *200
python multi-minimus.py *out
for f in *out; do cat $f.fasta $f.singletons.seq > $f.merged; done
cat *merged >> all-contigs.fa

