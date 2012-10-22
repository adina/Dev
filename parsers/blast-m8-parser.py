import sys

for line in open(sys.argv[1]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    identity = float(data[2])
    length = int(data[3])
    evalue = float(data[-2])

    if evalue < 1e-5:
        if length > 100:
            print line
