import sys, random

d = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    md5 = dat[0]
    taxa_id = dat[2]
    if taxa_id == '0' or taxa_id == 'none':
        continue
    else:
        if d.has_key(md5):
            d[md5].add(taxa_id)
        else:
            d[md5] = set()
            d[md5].add(taxa_id)

for key in d:
    print key, random.choice(list(d[key]))
    
