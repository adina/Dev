#! /usr/bin/env python
import screed, sys, itertools

paired_file = sys.argv[1]
paired_file1 = open(sys.argv[1] + '.pe1', 'w')
paired_file2 = open(sys.argv[1] + '.pe2', 'w')

for record in screed.open(paired_file):
    if record.name.endswith('/1'):
        paired_file1.write('@%s\n%s\n+\n%s\n' % (record.name, record.sequence, record.accuracy))
    else:
        paired_file2.write('@%s\n%s\n+\n%s\n' % (record.name, record.sequence, record.accuracy))
 
