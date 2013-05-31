import sys

d = {}

#normalized file stored in dict
for line in open(sys.argv[1]):
    line = line.rstrip().split(' ')
    if len(line) == 4:
        id = line[0]
        total_length = int(line[1])
        d[id] = total_length

coved = 0
total = 0
#normalize the actual blast
for line in open(sys.argv[2]):
    line = line.rstrip().split(' ')
    if len(line) == 4:
        id2 = line[0]
        total_aligned = int(line[1])
        total_length = int(line[2])
        norm_length = d[id2]
        if norm_length == 0:
            norm_fraction = 0
        else:
            norm_fraction = total_aligned/float(norm_length)
        coved += total_aligned
        total += norm_length 
        print id2, total_aligned, total_length, norm_length, norm_fraction

print coved, total, coved/float(total)
