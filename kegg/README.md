From BLAST output to gene summary:

python count_kos.py NOHUMAN_kegg.orf.count.tsv > NOHUMAN_kegg.orf.count.gene.tsv

From gene summary to include KO summary:
python kegg_genes_to_ko.py /mnt/research/germs/kegg/genes/ko/ko_genes.list NOHUMAN_kegg.orf.count.gene.tsv NOHUMAN_kegg.orf.count.ko.tsv

From Gene/Ko summary to KO counts:
python count_kos.py NOHUMAN_kegg.orf.count.ko.tsv > NOHUMAN_kegg.orf.count.ko.summary.tsv

From KO counts to include pathway:
python kegg_ko_to_path.py /mnt/research/germs/kegg/genes/ko/ko_pathway.list NOHUMAN_kegg.orf.count.ko.summary.tsv NOHUMAN_kegg.orf.count.ko.summary.path.tsv

Count pathways:
python count_paths.py NOHUMAN_kegg.orf.count.ko.summary.path.tsv > NOHUMAN_kegg.orf.count.ko.summary.path.summary.tsv
