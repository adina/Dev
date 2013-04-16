import sys, csv, operator

reader = csv.reader(open(sys.argv[1]), delimiter=" ");

sortedlist = sorted(reader, key=operator.itemgetter(3), reverse=True)
for x in sortedlist:
    print x[0], x[1], x[2], x[3]
