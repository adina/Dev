import sys

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    path = dat[0]
    gene = dat[1]
    if d.has_key(path):
        d[path].append(gene)
    else:
        d[path] = [gene]

for key in d.keys():
    print key + '\t' + '\t'.join(d[key])
