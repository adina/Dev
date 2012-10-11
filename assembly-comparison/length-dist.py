#! /usr/bin/env python
import screed, sys

file=sys.argv[1]

for n, record in enumerate(screed.open(file)):
    print len(record.sequence)
