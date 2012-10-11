import sys
import cPickle as pickle

d = pickle.load(open(sys.argv[1], 'rb'))

print len(d.keys())

for n, key in enumerate(d.keys()):
    if n == 0:
        print key, d[key]
