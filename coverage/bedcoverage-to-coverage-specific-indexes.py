import sys, numpy

'''Usage python bedcoverage-to-coverage.py list-of-contigs.txt metatassembly_transcripts.bed > foo'''

'''list-of-contigs:  Contig_1_300 (1-300 bp)'''


d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('_')
    if d.has_key(dat[0]):
        print 'hey'
    else:
        d[str(dat[0])] = (int(dat[1]), int(dat[2]))

d2 = {}
for line in open(sys.argv[2]):
    dat = line.rstrip().split('\t')
    contig = str(dat[0])
    if d.has_key(contig):
        start, end = d[contig][0], d[contig][1]
        contig_id = contig + "_" + str(start) + "_" + str(end)
        index = int(dat[-2])
        if index >= start and index <= end:
            cov_bp = int(dat[-1])
            if d2.has_key(contig_id):
                d2[contig_id].append(cov_bp)
            else:
                d2[contig_id] = [cov_bp]

sorted_keys = sorted(d2.keys())



for key in sorted_keys:
    l = d2[key]
    summy = 0
    median = numpy.median(l)
    avg = numpy.average(l)
    minl = min(l)
    maxl = max(l)
    for n, x in enumerate(l):
        if x > 0:
            summy += 1
    total = n + 1
    cov_rat = float(summy)/total
    print key, median, avg, minl, maxl, summy, total, cov_rat

