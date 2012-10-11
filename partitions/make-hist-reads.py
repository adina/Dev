import sys

#histogram:  prints out # of partitions with X genomes
#python make-hist.py [parsed pid file] > output

d = {}
d2 = {}
d3 = {}

for line in open(sys.argv[1]):
    line = line.split(' ')
    partition_count = int(line[0])
    read_count = int(line[1])
    read2_count = int(line[2])
    d[partition_count] = d.get(partition_count, 0) + 1
    if d2.has_key(partition_count):
        d2[partition_count] += read_count
        d3[partition_count] += read2_count
    else:
        d2[partition_count] = read_count
        d3[partition_count] = read2_count

for key in d.iterkeys():
    print key, d[key], d2[key], d3[key]
