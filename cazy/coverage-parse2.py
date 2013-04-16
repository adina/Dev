import sys

list = []
for line in open(sys.argv[1]):
    line = line.split('\t')
    query = line[0].split(']')[0] + ']'
    list.append(query)
    

for line in open(sys.argv[2]):
    dat = line.split(' ')
    if dat[0] in list:
        print line, 

