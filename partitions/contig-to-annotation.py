import sys
import cPickle as pickle

#python contig-to-annotation.py [saved dict] [blastout files]
'''filters contigs to 300 bp and makes dictionary with contig and best hit blastn annotation'''

all_blastout_files = sys.argv[2:]

d = {}

for file in all_blastout_files:
    file_in = open(file, 'r')
    for line in file_in:
        data = line.strip().split('\t')
        contig_id = data[0]
        contig_len = int(data[0].split('length_')[1].split('_')[0]) + 33 - 1 
        if contig_len > 300:
            annot = data[1]
            if d.has_key(contig_id):
                continue
            else:
                d[contig_id] = annot
    file_in.close()

pickle.dump(d, open(sys.argv[1], 'wb'))
