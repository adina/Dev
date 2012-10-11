import sys

d = {}
for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    contig = dat[0]
    ref = dat[1]
    evalue = float(data[-2])
    if evalue < 1e-5:
        if d.has_key(contig)
