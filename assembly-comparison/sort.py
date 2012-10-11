import sys
import operator

d = {}
d2 = {}
for line in open(sys.argv[1]):
    dat = line.rstrip().split(' ',1)
    d[dat[0]] = dat[1]
    numbers = dat[1].split(' ')
    total_sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    d2[dat[0]] = total_sum

sorted_keys = sorted(d2.iteritems(), key=operator.itemgetter(1))

for key in sorted_keys:
    print key[0], d[key[0]]
