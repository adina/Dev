import sys

for line in open(sys.argv[1]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    identity = float(data[3])

    if identity > 99:
        print line,
