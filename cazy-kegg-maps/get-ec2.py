import sys
import re

for line in open(sys.argv[1]):
    x = [m.start() for m in re.finditer('EC ', line.rstrip())]
    for each in x:
        print line[each+3:each+14].split(')')[0], 'red', ',', 'yellow'
