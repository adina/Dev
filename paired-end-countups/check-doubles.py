import sys

pe1 = sys.argv[1]
pe1singletons = open(pe1 + ".singletons", 'w')
pe1nonsingles = open(pe1 + ".nonsingles", 'w')

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    read = dat[0]
    gene_hit = dat[1]
    if d.has_key(read):
        d[read].append(line.rstrip())
    else:
        d[read] = [line.rstrip()]

for key in d.keys():
    if len(d[key]) > 1:
        for x in d[key]:
            pe1nonsingles.write('%s\n' %  x)
    else:
        pe1singletons.write('%s\n' % d[key][0])
