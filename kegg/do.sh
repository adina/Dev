file="$1"

echo $file

python count_kos.py $file > $file.gene.tsv
python kegg_genes_to_ko.py /mnt/research/germs/kegg/genes/ko/ko_genes.list $file.gene.tsv $file.count.ko.tsv
python count_kos.py $file.count.ko.tsv > $file.count.ko.summary.tsv
python kegg_ko_to_path.py /mnt/research/germs/kegg/genes/ko/ko_pathway.list $file.count.ko.summary.tsv $file.count.path.tsv
python count_paths.py $file.count.path.tsv > $file.count.path.summary.tsv