import sys, screed

d = {}

for record in screed.open(sys.argv[1]):
    name = record.name
    sequence = record.sequence
    d[name] = sequence

for line in open(sys.argv[2]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    identity = float(data[2])
    length = int(data[3])
    mm = int(data[4])
    gap = int(data[5])
    q_start = int(data[6])
    q_end = int(data[7])
    s_start = int(data[8])
    s_end = int(data[9])
    evalue = float(data[10])
    bit = float(data[11])
    print ">" + query
    print d[query]
