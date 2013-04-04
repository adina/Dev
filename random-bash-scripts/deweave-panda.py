import sys, screed

fp = open(sys.argv[1].split('.fasta')[0]+'.deweaved.fa', 'w')

for record in screed.open(sys.argv[1]):
    print >>fp, ">%s\\1" % (record.name)
    dat = record.sequence.split('-')
    print >>fp, '%s' % dat[0]
    print >>fp, ">%s\\2" % record.name 
    print >>fp, '%s' % dat[1]
