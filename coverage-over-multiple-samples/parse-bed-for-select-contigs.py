import sys

contigs = sys.argv[2:]

d = {}
for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    id, start, end, index, count = dat
    index = int(index)
    count = int(count)
    if id in contigs:
        if d.has_key(id):
            d[id][index] = count
        else:
            d[id] = {} 
            d[id][index] = count

for x in d.keys():
    for y in sorted(d[x].keys()):
        print x, y, d[x][y] 
