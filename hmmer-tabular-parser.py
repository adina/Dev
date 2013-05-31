import sys

for n, line in enumerate(open(sys.argv[1])):
    if line.startswith('#'):
        continue
    else:
        dat = line.rstrip().split(' ')
        dat = filter(None, dat)
        evalue = float(dat[4])
        if evalue < 1e-5:
            print line,
                     
