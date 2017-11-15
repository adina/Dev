import sys, screed

counter = 0
for n, record in enumerate(screed.open(sys.argv[1])):
    if n % 2 == 0:
        i = "f"
        counter += 1
    else:
        i = "r"
    print ">" + str(counter) + "_" + str(i) + '\t' + record.name
    print  record.sequence

