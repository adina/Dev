import sys

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    kegg_ko = dat[0]
    genes = dat[1:]
    d[kegg_ko] = genes

d2 = {}

for line in open(sys.argv[2]):
    dat= line.rstrip().split('\t')
    kegg_ko = dat[0]
    genes = dat[1:]
    d2[kegg_ko] = genes


for key in d:
    if d2.has_key(key):
        print key, len(d2[key]), len(d[key])
    else:
        continue
