import sys

d={}

for n, line in enumerate(open("/root/Dev/cazy-kegg-maps/FamInfo.txt")):
    if n>0:
        dat = line.rstrip().split('\t')
        cazy = dat[0]
        description = dat[-1]
        d[cazy] = description

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')[0]
    if d.has_key(dat):
        print dat, '\t', d[dat]
    else:
        print dat
