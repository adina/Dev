import collections, sys, csv, operator
import numpy

#python count-fams2.py cazy-list4.txt 

reader = csv.reader(open(sys.argv[1]), delimiter=" ")

list_fams = []
d_fam_coverage = {}
d_contig = {}

for contig, cazy, fam, coverage in reader:
    contig_new = contig.split(']')[0] + ']'
    d_contig[contig_new] = fam

for line in open(sys.argv[2]):
    line = line.rstrip().split(' ')
    contig_q = line[0]
    if d_contig.has_key(contig_q):
        fam_q = d_contig[contig_q]
        line.append(fam_q)
        new_line = ' '.join(line)
        print new_line
