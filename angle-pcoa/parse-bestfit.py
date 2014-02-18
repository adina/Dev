import sys

file = open(sys.argv[1])

d = {}

for line in file:
    dat = line.rstrip().split('\t')
    if d.has_key(dat[0]):
        d[dat[0]].append(dat[1])
    else:
        d[dat[0]] = [dat[1]]

for key in d:
    key_new = key.replace('$', '.')
    fp = open(sys.argv[1] + '.' + key_new + '.contigs', 'w')
    for x in d[key]:
        fp.write('%s\n' % x)

