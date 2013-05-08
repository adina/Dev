import gzip, sys 
import cPickle as pickle

#This will give you the contig annotations (md5 and ontology) for each contig
#python contig-to-function.py 550.cluster.aa90.mapping.gz 650.superblat.expand.lca.gz
#evalue 1e-5
#database = subsystem 14

d_cluster = {}

f1 = gzip.open(sys.argv[1], 'rb')

for line in f1:
    dat = line.split('\t')
    cluster = dat[0]
    contigs = dat[1:-1]
    d_cluster[cluster] = contigs

f2 = gzip.open(sys.argv[2], 'rb')

d_org = {}

for line in f2:
    dat = line.rstrip().split('\t')
    #md5 = dat[0]
    contig_orf = dat[1]
    lca = dat[-2]
    if contig_orf.startswith('aa90_'):
        contig_cluster = d_cluster[contig_orf]
        for each in contig_cluster:
            contig_id = each.split(']')[0] + ']'
            org_index = lca
    else:
        contig_id = contig_orf.split(']')[0] + ']'
        org_index = lca
    if d_org.has_key(contig_id):
        d_org[contig_id].append(org_index)
    else:
        d_org[contig_id] = [org_index]

pickle.dump(d_org, open("org.p", "wb"))
