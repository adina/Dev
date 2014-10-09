import sys, screed

l = []

for x in open(sys.argv[1]):
    l.append(x.rstrip())


for record in screed.open(sys.argv[2]):
    if record.name in l:
        print '>' + record.name
        print record.sequence
