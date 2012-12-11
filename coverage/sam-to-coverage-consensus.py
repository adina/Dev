import sys
import screed
import pysam
import numpy

samfile = pysam.Samfile(sys.argv[1], 'rb')
reference_file = sys.argv[2]

d = {}

for record in screed.open(reference_file):
    d[record.name] = len(record.sequence)

d2 = {}

list_top = []
for line in open(sys.argv[3]):
    line = line.rstrip().split(' ')[0]
    list_top.append(line)



for key in list_top:
    d2[key] = [[0,0,0,0]] * d[key]
    for pileupcolumn in samfile.pileup(key):    
        pos = pileupcolumn.pos
        coverage_at_pos = pileupcolumn.n
        d_bases = {'A':0, 'G':0, 'C':0, 'T':0}
  
        for pileupread in pileupcolumn.pileups:
            base = pileupread.alignment.seq[pileupread.qpos]
            d_bases[base] = d_bases.get(base) + 1
        d2[key][pos] = [d_bases['A'], d_bases['G'], d_bases['C'], d_bases['T']]

total_count = 0
count_threshold = 0

for key in d2.keys():
    length = len(d2[key])
    for n, each_pos in enumerate(d2[key]):
        if n > 100 and n < (length - 100):
            total_count += 1
            total = int(each_pos[0]) + int(each_pos[1]) + int(each_pos[2]) + int(each_pos[3])
            a = int(each_pos[0])/float(total)
            g = int(each_pos[1])/float(total)
            c = int(each_pos[2])/float(total)
            t = int(each_pos[3])/float(total)
            l = [a, g, c, t]
            max_num = max(l)
            if max_num > 0.95:
                count_threshold += 1
    print key, count_threshold, total_count, float(count_threshold)/total_count

            
