import sys

'''checks blastoutput for both sets of a primer pair'''

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    query = dat[0]
    hit = dat[1]
    if d.has_key(query):
        d[query].append(hit)
    else:
        d[query] = [hit]

d3 = {}

for key in d:
    d2 = {}
    uniq_l = set(d[key])
    if len(uniq_l) > 1:
        for x in uniq_l:
            new_x = x.rsplit('_', 1)[0]
            d2[new_x] = d2.get(new_x, 0) + 1
        for x in d2.keys():
            if d2[x] > 1:
                d3[x] = d3.get(x,0) + 1

for x in d3:
    print x, d3[x]
