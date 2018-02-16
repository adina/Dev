import sys
import itertools as iter

'''usage:  python venn.py <list of unique subsets> <output file>'''


my_list = []

for line in open(sys.argv[1]):
    dat = line.rstrip()
    my_list.append(dat)

length = len(my_list)

i = []

def get_combos(l, n):
    output = [":".join(items) for items in iter.combinations(l, r=n)]    
    return output

for x in range(1, length+1):
    l = get_combos(my_list, x)
    i += l

d = {}
i_copy = i 
for x in i:
    for y in i_copy:
        if x in y:
            if d.has_key(x):
                d[x].append(y)
            else:
                d[x] = [y]

fp = open(sys.argv[2], 'w')

for m, k in enumerate(d.keys()):
    fp.write('area_%s = ' % str(m))
    for n, each in enumerate(d[k]):
        if n == len(d[k]) - 1:
            fp.write("length(b[['%s']])" % str(each))
        else:
            fp.write("length(b[['%s']]) + " % str(each))
    fp.write('\n')

