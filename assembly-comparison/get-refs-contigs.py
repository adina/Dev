import sys

'''takes m8 output and gets top hits only'''
d = {}

for line in open(sys.argv[1]):
    data= line.split('\t')
    query_id = data[0]
    hit_id = data[1]
    contig_len = int(query_id.split('.')[-1])
    evalue = float(data[-2])
    if evalue < 1e-5:
        if d.has_key(hit_id):
            d[hit_id].append(contig_len)
        else:
            d[hit_id] = [contig_len]

d2 = {}

for key in d.keys():
    count1 = 0
    count2 = 0
    count3 = 0
    for x in d[key]:
        if x < int(sys.argv[2]):
            count1 += 1
        elif int(sys.argv[2]) <= x < int(sys.argv[3]):
            count2 +=1
        elif x >= int(sys.argv[3]):
            count3 += 1
    d2[key] = [count1, count2, count3]\

for key in d2.keys():
    print key, d2[key][0], d2[key][1], d2[key][2]
