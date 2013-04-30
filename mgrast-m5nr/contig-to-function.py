import gzip, sys 
import cPickle as pickle

#This will give you the contig annotations (md5 and ontology) for each contig
#python contig-to-function.py 550.cluster.aa90.mapping.gz 650.superblat.expand.ontology.gz
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

d_function = {}
d_ontology = {}
for line in f2:
    dat = line.rstrip().split('\t')
    #md5 = dat[0]
    contig_orf = dat[1]
    evalue = float(dat[4])
    database = dat[7]
    if evalue <= 1e-5 and database == '14':
        if contig_orf.startswith('aa90_'):
            contig_cluster = d_cluster[contig_orf]
            for each in contig_cluster:
                contig_id = each.split(']')[0] + ']'
                func_index = dat[5]
                ont_index = dat[6]
        else:
            contig_id = contig_orf.split(']')[0] + ']'
            func_index = dat[5]
            ont_index = dat[6]
        if d_function.has_key(contig_id):
            d_function[contig_id].append(func_index)
            d_ontology[contig_id].append(ont_index)
        else:
            d_function[contig_id] = [func_index]
            d_ontology[contig_id] = [ont_index]

pickle.dump(d_function, open("function.p", "wb"))
pickle.dump(d_ontology, open("ontology.p", "wb"))
