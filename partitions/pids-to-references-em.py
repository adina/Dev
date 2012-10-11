import sys
import cPickle as pickle
from collections import Counter

#python pids-to-reference.py [d_pids_to_reads] [d_reads_to_refs] [output]
'''prints (1) partition id (2) # of refs in pid (3) total # of reads in pid (4) reference count'''

d_pids_to_reads = pickle.load(open(sys.argv[1], 'rb'))
d_reads_to_refs = pickle.load(open(sys.argv[2], 'rb'))

d_pids_to_refs = {}

fp2 = open(sys.argv[3]+'.log', 'w')

fp2.write('loaded in dicts\n')
fp2.write('starting to iterate through pids_to_reads\n')

count = 0
for key, reads in d_pids_to_reads.iteritems():
    count += 1
    for each_read in reads:
	reference = d_reads_to_refs.get(each_read, ['none'] )[0]
        if d_pids_to_refs.has_key(key):
            d_pids_to_refs[key].append(reference)
        else:
            d_pids_to_refs[key] = [reference]
    if count % 100 == 0:
        fp2.write('...%d' % count)


fp2.write('saving dictionary\n')

pickle.dump(d_pids_to_refs, open(sys.argv[3] + '.p', 'wb'))

fp2.write('printing file\n')

fp = open(sys.argv[3] + '.txt', 'w')

for x in d_pids_to_refs.keys():
    c = Counter(d_pids_to_refs[x])
    fp.write('%s %d %d\t' % (x, len(c.keys()), sum(c.values())))
    for ref in c.keys():
        fp.write('%s %d ' % (ref, c[ref]))
    fp.write('\n')
    
