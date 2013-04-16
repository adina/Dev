import sys

#python insert-cov.py <cov-text-file> <cazy text file>

d = {}
for line in open(sys.argv[1]):
    line = line.rstrip().split(' ')
    d[line[0]] = line[1]

for line in open(sys.argv[2]):
    dat = line.rstrip().split(' ')
    contig = dat[0].split(']_')[0] + ']'
    coverage = d[contig]
    dat.append(coverage)
    print " ".join(dat)
