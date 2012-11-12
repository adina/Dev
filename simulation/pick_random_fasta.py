#!/usr/bin/env python
import sys
import random



filein = sys.argv[1]
fileout = sys.argv[2]
num_to_choose = int(sys.argv[3])

fh = open(filein,'r')
fw = open(fileout,'w')


head_list=[]
seq_list = []

seq=''
for line in fh:
    line = line.rstrip()
    if line !='':

	if line[0] == '>':
        	if seq !='':
            		seq_list.append(seq)
            
        	head = line
        	head_list.append(head)
        	seq = ''
    	else:
        	seq = seq+line
        
        
seq_list.append(seq)


number_seq = len(head_list)
print number_seq
print num_to_choose
to_choose_list = random.sample(range(number_seq),num_to_choose)
#to_choose_list = random.sample(xrange(2000),200)


for i in to_choose_list:
    fw.write(head_list[i]+'\n')
    fw.write(seq_list[i]+'\n')


