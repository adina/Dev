import sys

for line in open(sys.argv[1]):
    line = line.rstrip().split('.ass.')
    print line[0], line[1]
