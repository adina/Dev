import sys
import screed
import pysam

#takes bowtie maps and calculates coverage for contigs.
#output = contig id, base pair coverage median, contig length, read coverage
  
samfile = pysam.Samfile(sys.argv[1], 'rb')

count = 0
for n, alignedread in enumerate(samfile.fetch()):
    count += 1

print count
