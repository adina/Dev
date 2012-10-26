import sys

for line in open(sys.argv[1]):
    if int(line.rstrip().split(' ')[1]) == 3:
        print line.rstrip().split(' ')[0]
    
