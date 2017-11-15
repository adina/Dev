import sys

'''checks blastoutput for both sets of a primer pair'''

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    query = dat[0]
    hit = dat[1]
    if d.has_key(hit):
        d[hit].append(query)
    else:
        d[hit] = [query]

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
                if d3.has_key(key):
                    d3[key].append(x)
                else:
                    d3[key] = [x]
for key in d3:
    print key + '\t' + '\t'.join(d3[key])

