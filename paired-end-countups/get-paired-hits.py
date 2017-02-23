import sys

pe1 = sys.argv[1]
pe2 = sys.argv[2]

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    read = dat[0]
    gene_hit = dat[1]
    if d.has_key(read):
        d[read].append(gene_hit)
    else:
        d[read] = [gene_hit]

for line in open(sys.argv[2]):
    dat = line.rstrip().split('\t')
    read = dat[0]
    gene_hit = dat[1]
    pe1_check_read = False
    pe1_check_hit = False
    if d.has_key(read):
        pe1_check_read = True
        if gene_hit in d[read]:
            pe1_check_hit = True
    if pe1_check_read is True and pe1_check_hit is True:
        print line,
