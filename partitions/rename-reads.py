import screed, sys
import cPickle as pickle

d1 = pickle.load(open(sys.argv[2], 'rb'))
d2 = pickle.load(open(sys.argv[3], 'rb'))

fp = open(sys.argv[1], 'w')

for file in sys.argv[4:]:
    for n, record in enumerate(screed.open(file)):
        print >> fp, '>' + record.name + '_' + d1[record.name] + '_' + d2[record.name]
        print >> fp, record.sequence
                
                    

