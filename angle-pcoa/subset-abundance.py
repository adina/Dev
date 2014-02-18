import sys

l = []
for line in open(sys.argv[1]):
    l.append(line.rstrip())

for n, line in enumerate(open(sys.argv[2])):
    if n == 0:
        print line.rstrip()
    else:
        dat = line.rstrip().split('\t')
        if dat[0] in l:
            print line.rstrip()
