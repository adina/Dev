import sys, re

for n, line in enumerate(open(sys.argv[1])):
    if line.startswith("#"):
        if n == 1:
            dat = line.rstrip().split(' ')
            foo = dat[1].split('_')
            dat[1]=  foo[1] + '_' + foo[2]
            print ' '.join(dat)
        else:
            print line,
    else:
        dat = line.rstrip().split('\t')
        foo = dat[0].split('_')
        dat[0]=  foo[1] + '_' + foo[2]
        dat[8] = re.sub("%5D", "", dat[8])
        dat[8] = re.sub("%5B", "", dat[8])
        dat[8] = re.sub("%28", "", dat[8])
        dat[8] = re.sub("%29", "", dat[8])
        print '\t'.join(dat)
    


