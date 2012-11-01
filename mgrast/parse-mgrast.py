import sys

def striplist(l):
    return([x.strip() for x in l])

for line in open(sys.argv[1]):
    dat = line.rstrip().split(' ')
    try:
        int(dat[-1])
        dat2 = line.rstrip().split(' ')
        dat2 = filter(None, dat2)
        annotation =' '.join(dat2[:-2])
        print annotation, '\t', dat2[-2], '\t', dat2[-1]
            
    except:
        continue
