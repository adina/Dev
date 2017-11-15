import sys

'''checks blastoutput for both sets of a primer pair'''

d = {}
d2 = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    query = dat[0]
    query_gen = query.split('_')[0]
    hit = dat[1]
    info = hit
    if d.has_key(query_gen):
        d[query_gen].append(query)
        d2[query_gen].append(hit)
    else:
        d[query_gen] = [query]
        d2[query_gen] = [hit]

for key in d:
    uniq_l = set(d[key])
    if len(uniq_l) > 1:
        #print key, uniq_l, set(d2[key])
        for x in set(d2[key]):
            print key
    
