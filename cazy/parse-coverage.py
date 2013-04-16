import sys

for line in open(sys.argv[1]):
    line = line.rstrip().split(' ')
    cov_kmer = line[0].split('[cov=')[1][:-1]
    cov_reads = float(line[1])
    print cov_kmer, cov_reads
