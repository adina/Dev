import sys

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    query = dat[0]
    cazy = dat[1]
    cazy_fam = dat[2].split('FAM=')[1].split(' ')[0]
    if cazy_fam == '':
        cazy_fam = 'nofam'
    print query, cazy, cazy_fam
