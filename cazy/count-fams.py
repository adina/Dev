import collections, sys, csv, operator
import numpy

#python count-fams.py cazy-list4.txt FamInfo.txt test

reader = csv.reader(open(sys.argv[1]), delimiter=" ")

list_fams = []
d_fam_coverage = {}
d_contig = {}

for contig, cazy, fam, coverage in reader:
    d_contig[contig] = fam
    fam = fam.split(',')
    for x in fam:
        list_fams.append(x)
        if d_fam_coverage.has_key(x):
            d_fam_coverage[x].append(float(coverage))
        else:
            d_fam_coverage[x] = [float(coverage)]

d_average = {}
for x in d_fam_coverage.keys():
    d_average[x] = numpy.average(d_fam_coverage[x])

d_fam_annotation = {}
for n, line in enumerate(open(sys.argv[2])):
    if n > 0:
        dat = line.rstrip().split('\t')
        cazy_fam = dat[0]
        description = dat[-1]
        d_fam_annotation[cazy_fam] = description

c_fams = collections.Counter(list_fams)

GH = {}
GT = {}
PL = {}
CE = {}
AA = {}
CMB = {}

list_enzymes_classes = ['GH', 'GT', 'PL', 'CE', 'AA', 'CMB']
d_map = {'GH':GH, 'GT':GT, 'PL':PL, 'CE':CE, 'AA':AA, 'CMB':CMB}

for key in c_fams.keys():
    for enzyme in list_enzymes_classes:
        if key.startswith(enzyme):
            dict_to_add = d_map[enzyme]
            dict_to_add[key] = c_fams[key]

fp = open(sys.argv[3], 'w')
for value in d_map.values():
    sorted_x = sorted(value.iteritems(), key=operator.itemgetter(1), reverse=True)
    for each in sorted_x:
        print >>fp, '%s\t%f\t%f\t%s' % (each[0], each[1], d_average[each[0]], d_fam_annotation[each[0]])

