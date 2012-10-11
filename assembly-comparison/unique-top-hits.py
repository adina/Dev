import sys

'''takes m8 output and gets top hits only'''
d = {}

for line in open(sys.argv[1]):
    data= line.split('\t')
    query_id = data[0]
    hit_id = data[1]
    if d.has_key(query_id):
        continue
    else:
        d[query_id] = 1
        print line,
