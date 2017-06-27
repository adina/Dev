import sys

index_of_import = 1
d_gene = {}

f = sys.argv[1]

d = {}

for n, line in enumerate(open(f)):
    if n == 0:
        ids = line.rstrip().split('\t')
        number_of_samp = len(ids)
    else:
        dat = line.rstrip().split("\t")
        counter_id = dat[index_of_import]
        for x in counter_id.split(','):
            if d.has_key(x):
                dat[index_of_import+1:] = map(int, dat[index_of_import+1:])
                new_sum = [a + b for a,b in zip(d[x], dat[index_of_import+1:])]
                d[x] = new_sum
            else:
                dat[index_of_import+1:] = map(int, dat[index_of_import+1:])
                d[x] = dat[index_of_import+1:]

print "\t".join(ids)

for key in d.keys():
    d[key] = map(str, d[key])
    print key +"\t" + "\t".join(d[key])
