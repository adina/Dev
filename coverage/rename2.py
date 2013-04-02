#! /usr/bin/env python
import screed, sys

infile=sys.argv[1]
prefix=sys.argv[2]

for n, record in enumerate(screed.open(infile)):
    contig = record.name.split('\t')[0]
    new_name = '%s_%d' % (prefix, n)
    print '>' + new_name
    print record.sequence
