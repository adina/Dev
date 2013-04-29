import sys

#python count-hits.py output list-cov.txt *cov
#Use this for Kirsten's data where file names need to be mapped to something else


fp = open(sys.argv[1], 'w')
map = open(sys.argv[2])
files = sys.argv[3:]
total_files = len(files)
d = {}

d_map = {}

for line in map:
    line = line.rstrip().split(' ')
    d_map[line[0]] = line[1]

key_order = sorted(d_map.keys())

for n, sample in enumerate(key_order):
    file = d_map[sample]
    print file
    for line in open(file):
        line = line.split(' ') 
        contig = line[0]
        max_reads = int(line[4])
        if d.has_key(contig):
            d[contig][n] = max_reads
        else:
            d[contig] = [0]*total_files
            d[contig][n] = max_reads

for x in sorted(key_order):
    fp.write('\t%s' % x)
fp.write('\n')

for key in d.keys():
    fp.write('%s\t' % key)
    for i in range(total_files):
        fp.write('%d\t' % d[key][i])
    fp.write('\n')

        

