import csv
import sys, os.path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pylab
from pylab import plot, savefig, hist, axis, xlabel, ylabel, title
import ast


'''usage python x-y-plot.py [output of sam-to-coverage-bases.py] [nth contig] [out]'''
filein = open(sys.argv[1], 'r')

list_all = []
'''this reads in a printed list [1, 2, 3, 4] into a literal list'''
for n, line in enumerate(filein):
    test = line.rstrip().split(' ', 1)[1]
    test = ast.literal_eval(test)
    list_all.append(test)

x = []
a_data = []
g_data = []
c_data = []
t_data = []
n_data = []

for n, each_pos in enumerate(list_all):
    x.append(n)
    #total = int(each_pos[0]) + int(each_pos[1]) + int(each_pos[2]) + int(each_pos[3])
    a = int(each_pos[0])#/float(total)
    g = int(each_pos[1])#/float(total)
    c = int(each_pos[2])#/float(total)
    t = int(each_pos[3])#/float(total)
    n = int(each_pos[4])#/float(total)
    #print a, a_data
    #print g, g_data
    a_data.append(a)
    g_data.append(g)
    c_data.append(c)
    t_data.append(t)
    n_data.append(n)
#print len(a_data), len(g_data)

plt.plot(x, a_data, 'ro', x, g_data, 'bo', x, c_data, 'go', x, t_data, 'co')
#plt.axis([1200,1400,0,1])
#plt.show()
plt.savefig(sys.argv[2])

 
