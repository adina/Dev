import sys

d = {}
for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    d[dat[0].split('_')[1]] = dat[1]


for n, line in enumerate(open(sys.argv[2])):
    if n == 0:
        dat = line.rstrip().split('\t')
        for n, x in enumerate(dat):
            if n == 0:
                print 'ID\t',
            if n > 0:
                id1 = d[x.split('_')[0]]
                id2 = x.split('_')[-2]
                id = str(id1) + '_' + id2
                print id + '\t',
        print '\n',
    else:
        print line, 
        
