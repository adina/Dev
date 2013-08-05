import sys, screed

print "@HD\tVN:1.0\tSO:unsorted"
for record in screed.open(sys.argv[1]):
    print "@SQ\tSN:" + record.name + "\tLN:" + str(len(record.sequence))
