import sys

d = {}
for line in open(sys.argv[1]):
    line = line.rstrip().split('\t')
    orf = line[1]
    evalue = float(line[4])
    if evalue < 1e-3:
        d[orf] = 1

for key in d.keys():
    print key
