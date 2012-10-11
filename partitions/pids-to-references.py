import sys
import cPickle as pickle
from collections import Counter

#python pids-to-reference.py [d_pids_to_reads] [d_reads_to_refs] [output]
'''prints (1) partition id (2) # of refs in pid (3) total # of reads in pid (4) reference count'''

d_pids_to_reads = pickle.load(open(sys.argv[1], 'rb'))
d_reads_to_refs = pickle.load(open(sys.argv[2], 'rb'))

d_pids_to_refs = {}

for key in d_pids_to_reads.keys():
    for each_read in d_pids_to_reads[key]:
        if each_read in d_reads_to_refs.keys():
            reference = d_reads_to_refs[each_read]
        else:
            reference = 'none'
        if key in d_pids_to_refs.keys():
            d_pids_to_refs[key].append(reference)
        else:
            d_pids_to_refs[key] = [reference]

sorted_keys = sorted(d_pids_to_refs.keys(), key=lambda x: int(x))

fp = open(sys.argv[3], 'w')
for x in sorted_keys:
    c = Counter(d_pids_to_refs[x])
    fp.write('%s %d %d\t' % (x, len(c.keys()), sum(c.values())))
    for ref in c.keys():
        fp.write('%s %d ' % (ref, c[ref]))
    fp.write('\n')
    
