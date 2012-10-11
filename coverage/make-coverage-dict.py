import cPickle as pickle
import sys

d = {}

files = sys.argv[1:]

for file in files:
    for line in open(file):
        dat = line.rstrip().split(' ')
        contigid = dat[0]
        coverage = float(dat[1])
        d[contigid] = coverage

pickle.dump(d, open("coverage-dict.p", 'wb'))
