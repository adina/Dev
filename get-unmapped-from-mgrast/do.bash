#gzip -d 650*gz
#gzip -d 350*gz
python get-list-of-hits.py 650*sims > list-of-orfs-hits.txt
java -jar /adina/Dev/remove-reads/Clustering.jar filter-seqs list-of-orfs-hits.txt 550*.faa True > noannotation-orfs.faa
