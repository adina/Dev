import sys, screed
import collections

#get list of cluster ids to grab
list = []
for line in open(sys.argv[1]):
    line = int(line.rstrip())
    list.append(line)

last_key = ''

d = {}

for n, line in enumerate(open(sys.argv[2])):
    if line.startswith('>'):
        cluster = int(line.rstrip().split(' ')[1])
        lastkey = cluster
    elif line.rstrip().endswith('*'):
        if lastkey in list:
            id = line.split('>')[1].split('...')[0]
            print id
        
