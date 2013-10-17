import sys
import random 
from random import choice

for line in open(sys.argv[1]):
    id = line.split(' ')[0]
    cazy_fam = line.split('FAM=')[1].split(' ')[0]
    t1 = line.split('RANK1=')[1].split(' ')[0]
    t2 = line.split('RANK2=')[1].split(' ')[0]
    t3 = line.split('RANK3=')[1].split(' ')[0]
    cazy_list = cazy_fam.split(',')
    cazy_fam = choice(cazy_list)
    print id, cazy_fam, t1, t2, t3, "1"
