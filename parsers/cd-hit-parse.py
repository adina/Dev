import sys, screed

fp = open(sys.argv[2], 'w')

for record in screed.open(sys.argv[1]):
    sequence = record.sequence
    count_seq = sequence.count('>')
    if count_seq > 1:
        sequence = sequence.split('>')
        for x in sequence:
            if 'iowa' in x:
                x = x.split('...')
                fp.write('%s\t' % x[0])
        fp.write('\n')
