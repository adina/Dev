import sys
import cPickle as pickle
import collections
import operator

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def sort_dict_by_value(d):
    sorted_list = sorted(d.iteritems(), key=operator.itemgetter(1))
    best_hit = sorted_list[0][0]
    return best_hit

annotation_func_d = pickle.load(open("/adina4/m5nr/annotations/function_map.p", "rb"))
annotation_ont_d = pickle.load(open("/adina4/m5nr/annotations/ontologies.p", "rb"))

d_function = pickle.load(open("function.p", "rb"))
d_ontology = pickle.load(open("ontology.p", "rb"))

fp = open(sys.argv[1] + ".md5", 'w')
fp2 = open(sys.argv[1] + ".ann", 'w')


for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    dat2 = line.rstrip().split('\t')
    contig = dat[0]
    if d_function.has_key(contig):
        func_list = collections.Counter(d_function[contig])
        ont_list = collections.Counter(d_ontology[contig])
        best_hit_func = sort_dict_by_value(func_list)
        best_hit_ont = sort_dict_by_value(ont_list)
        best_hit_func_ann = annotation_func_d[best_hit_func]
        best_hit_ont_ann = str(annotation_ont_d[best_hit_ont])
    
    else:
        best_hit_func, best_hit_func_ann = "N\A", "N\A"
        best_hit_ont, best_hit_ont_ann = "N\A", "N\A"
    dat.append(best_hit_func)
    dat.append(best_hit_ont)
    dat2.append(best_hit_func_ann)
    dat2.append(best_hit_ont_ann)
    fp.write("%s\n" % ("\t".join(dat)))
    fp2.write("%s\n" % ("\t".join(dat2)))
    
