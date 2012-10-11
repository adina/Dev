import sys, screed
import cPickle as pickle

#python reads-to-pids.py [partitioned fastas]

'''creates a dictionary of reads to pids'''

d = {}
all_partition_files = sys.argv[2:]
for file in all_partition_files:
    file_in = open(file, 'r')
    for record in screed.open(file):
        readid = record.name.split('\t')[0]
        pid = record.name.split('\t')[1]
        d[readid] = pid
    file_in.close()

pickle.dump(d, open(sys.argv[1], 'wb'))



