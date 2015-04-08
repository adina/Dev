import sys

for line in open(sys.argv[1]):
    if line.startswith("#"):
        print line,
    else:
        dat = line.rstrip().split('\t')
        if dat[2] == "CDS":
            print line,

