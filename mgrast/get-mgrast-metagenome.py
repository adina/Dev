import sys

for line in open(sys.argv[1]):
    #curl "http://api.metagenomics.anl.gov/1/download/mgm4461125.3?file=050.1"
    print '''curl "http://api.metagenomics.anl.gov/1/download/mgm''' + line.rstrip() + '''?file=050.1" > ''' + line.rstrip() + '.fna'

