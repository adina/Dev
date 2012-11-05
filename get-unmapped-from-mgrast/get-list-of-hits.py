import sys

d = {}
for line in open(sys.argv[1]):
    line = line.rstrip().split('\t')
    orf = line[0]
    d[orf] = ''
for key in d.keys():
    print key
