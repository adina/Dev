import sys
import cPickle as pickle

#reads-to-references.py [bowtie map] [pickled dict saved]
'''creates a pickled dictionary where keys are read names and values are the lsit of reference ids with 0 mismatches'''



d = {}

for line in open(sys.argv[1]):
    data = line.strip().split('\t')
    read_id = data[0].split(' ')[0]
    reference = data[2]
    if d.has_key(read_id):
        d[read_id].append(reference)
    else:
        d[read_id] = [reference]

pickle.dump(d, open(sys.argv[2], 'wb'))
