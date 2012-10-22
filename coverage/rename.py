#! /usr/bin/env python
import screed, sys
import cPickle as pickle

infile=sys.argv[1]

d = pickle.load(open(sys.argv[2], 'rb'))

for n, record in enumerate(screed.open(infile)):
    contig = record.name.split('\t')[0]
    if d.has_key(contig):
        coverage = d[contig]
    else:
        coverage = 0
    new_name = '%s_[cov=%f]' % (record.name.split('\t')[0], coverage)
    print '>' + new_name
    print record.sequence
