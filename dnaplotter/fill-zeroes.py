import sys

d = {}

length_of_contig = int(sys.argv[2])

for line in open(sys.argv[1]):
    dat = line.rstrip().split(' ')
    if len(dat) == 2:
        i = int(dat[0])
        count = int(dat[1])
        d[i] = count
    else:
        continue

for x in range(1, length_of_contig+1):
    if x in d.keys():
        print d[x]
    else:
        print int(0)

