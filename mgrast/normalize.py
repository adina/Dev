import sys

giant_list = []

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    giant_list.append(dat)

total_1 = 0
total_2 = 0

for x in giant_list:
    total_1 += int(x[1])
    total_2 += int(x[2])

for x in giant_list:
    print x[0], '\t', int(x[1])/float(total_1), '\t', int(x[2])/float(total_2), '\t',  int(x[1]), '\t', int(x[2])
