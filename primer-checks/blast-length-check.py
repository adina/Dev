import sys

for line in open(sys.argv[1]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    l_primer = float(data[2])
    identity = float(data[3])
    length = int(data[4])
    evalue = float(data[-2])

    if l_primer == length:
        print line,
