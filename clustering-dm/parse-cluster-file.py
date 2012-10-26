import sys, screed
import collections

last_key = ''

d = {}

for n, line in enumerate(open(sys.argv[1])):
    if line.startswith('>'):
        cluster = int(line.rstrip().split(' ')[1])
        last_key = cluster
    else:
        id = line.split('>')[1].split('_')[0]
        if d.has_key(last_key):
            d[last_key].append(id)            
        else:

            d[last_key] = [id]

#prints cluster#, # of samples in cluster
for key in d.keys():
    x = collections.Counter(d[key])
    print key, len(x.keys())


