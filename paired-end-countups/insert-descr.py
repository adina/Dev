import sys

d = {}
for line in open(sys.argv[1], 'rU'):
    dat = line.rstrip().split(' ')
    gene_id = dat[0].split('\t')[0]
    gene_name = dat[-1].split('\t')[-1]
    d[gene_id] = gene_name

for n, line in enumerate(open(sys.argv[2], 'rU')):
    if n == 0:
        print line,
    if n > 0:
        dat = line.rstrip().split('\t')
        dat.insert(1, d[dat[0]])
        print '\t'.join(dat)
