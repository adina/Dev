import sys

d_old = {}
for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    id = dat[0]
    primers = dat[1:]
    d_old[id] = [primers, ['none']]

for line in open(sys.argv[2]):    
    dat= line.rstrip().split('\t')
    id = dat[0]
    primers = dat[1:]
    if d_old.has_key(id):
        d_old[id][1] = primers
    else: 
        d_old[id] = [['none'], primers]

for key in d_old:
    print key + '\t' + ','.join(d_old[key][0]) + '\t'+ ','.join(d_old[key][1])
