import sys

for line in open(sys.argv[1], 'rU'):
    dat = line.rstrip().split(',')
    print ">" + dat[0] + "_" + "f"
    print dat[6]
    print ">" + dat[0] + "_" + "r"
    print dat[7]
    
