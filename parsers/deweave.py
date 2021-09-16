import sys, screed

basename = sys.argv[1]
fp_1 = open(basename + '.pe1.fastq', 'w')
fp_2 = open(basename + '.pe2.fastq', 'w')

for n, record in enumerate(screed.open(sys.argv[1])):
    if n % 2 == 0:
        fp_1.write('@%s %s\n' % (record.name, record.annotations))
        fp_1.write('%s\n' % record.sequence)
        fp_1.write('+\n')
        fp_1.write('%s\n' % record.accuracy)

    else:
        fp_2.write('@%s %s\n' % (record.name, record.annotations))
        fp_2.write('%s\n' % record.sequence)
        fp_2.write('+\n')
        fp_2.write('%s\n' % record.accuracy)
