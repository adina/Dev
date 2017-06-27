import sys

for n, line in enumerate(open(sys.argv[1])):
    if n > 0:
        dat = line.rstrip().split('\t')
        if len(dat[2].split(',')) > 1:
            print dat[2]
