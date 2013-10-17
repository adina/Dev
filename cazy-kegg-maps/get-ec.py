import sys
import re

fp = open("kegg.txt", 'w')

for line in open(sys.argv[1]):
    x = [m.start() for m in re.finditer('EC ', line.rstrip())]
    fp.write('%s' % line.split('\t')[0])
    for each in x:
        fp.write('\t%s' % line[each+3:each+14].split(')')[0])
    fp.write('\n')
