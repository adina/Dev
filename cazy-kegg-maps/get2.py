import sys

d={}

for n, line in enumerate(open("FamInfo.txt")):
    if n>0:
        dat = line.rstrip().split('\t')
        cazy = dat[0]
        description = dat[-1]
        d[cazy] = description

for line in open("list2.txt"):
    if d.has_key(line.rstrip()):
        print line.rstrip(), '\t', d[line.rstrip()]
    else:
        print line.rstrip()
