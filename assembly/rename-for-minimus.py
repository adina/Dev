import sys
import screed

for n, record in enumerate(screed.open(sys.argv[1])):
    if len(record.sequence) >= 200:
        print '>' + record.name + '_' + str(n)
        print record.sequence 
