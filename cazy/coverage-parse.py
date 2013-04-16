import sys

for line in open(sys.argv[1]):
    dat = line.split(' ')
    contig = dat[0].split('cov=')[1].split(']')[0]
    coverage = dat[1]
    print contig, coverage
