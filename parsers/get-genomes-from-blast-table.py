import sys, screed

d = {}

for record in screed.open(sys.argv[1]):
    name = record.name.split(' ')[0]
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
    s_min = min(s_start, s_end)
    s_max = max(s_start, s_end)
    evalue = float(data[10])
    bit = float(data[11])
    if d.has_key(hit):
        print ">" + hit
        print d[hit][s_min - 1:s_max]
