import sys
import screed

prefix = str(sys.argv[2])

for n, record in enumerate(screed.open(sys.argv[1])):
    if len(record.sequence) >= 200:
        print '>' + prefix + '_' + str(n) + '\t' + record.name 
        print record.sequence 
