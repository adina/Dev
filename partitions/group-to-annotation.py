import sys, pickle
from collections import Counter

#group#, total#references, total#contigs, reference, count

d_group_to_annotation = pickle.load(open(sys.argv[1], 'rb'))

d = {}

for key in d_group_to_annotation.keys():
    groupid = key.split('_')[0][5:]
    if d.has_key(groupid):
        d[groupid].append(d_group_to_annotation[key])
    else:
        d[groupid] = [d_group_to_annotation[key]]

sorted_keys = sorted(d.keys(), key=lambda x: int(x))

fp = open(sys.argv[2], 'w')
for x in sorted_keys:
    c = Counter(d[x])
    fp.write('%s %d %d\t' % (x, len(c.keys()), sum(c.values())))
    for ref in c.keys():
        fp.write('%s %d ' % (ref, c[ref]))
    fp.write('\n')
    
