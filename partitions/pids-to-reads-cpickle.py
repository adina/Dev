import sys
import cPickle as pickle

#python pids-to-reads.py [reads-to-pids] [pids-to-reads]
'''loads in pickled dictionary and inverses it to a pickled dictionary'''

def dict_inverse(d):
    new_d = {}
    for key, value in d.iteritems():
        if value in new_d.iterkeys():
            new_d[value].append(key)
        else:
            new_d[value] = [key]
    return new_d

d1 = pickle.load(open(sys.argv[1], 'rb'))
d2 = dict_inverse(d1)

pickle.dump(d2, open(sys.argv[2], 'wb'))

