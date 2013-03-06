import sys
from screed.fasta import fasta_iter

def read_partition_file(fp):
    for n, record in enumerate(fasta_iter(fp, parse_description=False)):
        name = record['name']
        name, partition_id = name.rsplit('\t', 1)
        yield n, name, int(partition_id), record['sequence']

select_pid = [6479, 3]

d = {}

for n, name, pid, seq in read_partition_file(open(sys.argv[1])):
    if pid in select_pid:
        dat = [name, pid, seq] 
        if d.has_key(pid):
            d[pid].append(dat)
        else:
            d[pid] = [dat]

file_d = {}
for n, x in enumerate(d.keys()):
    fp = open('pid-%s.fa' % x, 'w')
    file_d[x] = fp

for x in d.keys():
    outfp = file_d[x]
    for y in d[x]:
        outfp.write('>%s\t%s\n%s\n' % (y[0], y[1], y[2]))
