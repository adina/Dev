import sys, numpy

#python *.py [coverage bed per base file] > [output]

d = {}
d2 = {}

for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    ref = dat[0] + "_" + str(dat[1]) + "_" + str(dat[2])
    ann = dat[3]
    subs = dat[4]
    count = int(dat[7])
    if d.has_key(ref):
        d[ref].append(count)
    else:
        d[ref] = [count]
        d2[ref] = (ann, subs)

for key in d:
    coverage_list = d[key]
    sum_list = sum(coverage_list)
    if sum_list == 0:
        continue
    else:
        median = str(numpy.median(coverage_list))
        average = str(numpy.average(coverage_list))
        min_val = str(min(coverage_list))
        max_val = str(max(coverage_list))
        to_print = [key, d2[key][0], d2[key][1], median, average, min_val, max_val]
        print '\t'.join(to_print)
