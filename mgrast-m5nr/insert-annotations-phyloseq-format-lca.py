import sys
import cPickle as pickle
import collections
import operator

def sort_dict_by_value(d):
    sorted_list = sorted(d.iteritems(), key=operator.itemgetter(1))
    best_hit = sorted_list[0][0]
    return best_hit

d_org = pickle.load(open("org.p", "rb"))

fp = open(sys.argv[1] + ".org", 'w')


for n, line in enumerate(open(sys.argv[1])):
    if n > 0:
        dat = line.rstrip().split('\t')
        contig = dat[0]
        if d_org.has_key(contig):
            lca = d_org[contig]
            c = collections.Counter(lca)
            best_hit = sort_dict_by_value(c)
            fp.write('%s' % contig)
            if len(best_hit.split(';')) == 8:
                for x in best_hit.split(';'):
                    fp.write('\t%s' % x)
                fp.write('\n')
        else:
            fp.write('%s\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\n' % contig)
    
