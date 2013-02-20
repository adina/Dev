import sys
from Bio import SeqIO

genome=SeqIO.parse(sys.argv[1], 'genbank')

d = {}
counter = 0
list_features = []

d2 = {}
for x in genome:
    #print x
    #print x.id
    d2[x.id] = x.description
    #print x.description
    #print x.name
    #print len(x.seq)
    dict_id = x.id + '_len_' + str(len(x.seq))
    #print dict_id
    #print x.features
    #print x.annotations["taxonomy"]

    for y in x.features:
        if y.type == 'CDS':
            #print y.location.start.position
            #print y.location.end.position
            #print y.strand
            for z in y.qualifiers["product"]:
                list_features.append(z)
                counter += 1
                print counter
                
                if 'phage' in z:
                    #print dict_id
                    #print counter, x.id
                    #print z
                    #print y.qualifiers["translation"]
                    #print y.strand
                    start = y.location.start.position
                    end = y.location.end.position
                    #print x.seq[start:end]
                    #print x.annotations["source"]
                    phage_info = (counter, z, start, end)
                    #print counter, phage_info, list_features[counter-1]
                    if d.has_key(dict_id):
                        d[dict_id].append(phage_info)
                    else:
                        d[dict_id] = [phage_info]
                    #print list_features, len(list_features)

fp = open(sys.argv[2], 'w')   

for key in d.keys():
    print key
    id = key.split('_len_')[0]
    length = int(key.split('_len_')[1])
    for x in d[key]:


        fp.write('%s\t%s\t%d' % (key, d2[id], length))
        fp.write('\t%d\t%d' % (x[2], x[3]))
        fp.write('\t%s\t%s\t%s\t%s\t%s\n' % (list_features[x[0]-1],list_features[x[0]-3], list_features[x[0]-2], list_features[x[0]], list_features[x[0]+1]))
#print d2

