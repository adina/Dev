import csv
import sys, os.path
import matplotlib
import matplotlib.pyplot as plt
import pylab
from pylab import plot, savefig, hist, axis, xlabel, ylabel, title
import ast

filein = open(sys.argv[1], 'r')

for n, line in enumerate(filein):
    if n == int(sys.argv[2]):
        test = line.rstrip().split(' ', 1)[1]
        test = ast.literal_eval(test)

x = []
a_data = []
g_data = []
c_data = []
t_data = []
    
for n, each_pos in enumerate(test):
    x.append(n)
    total = int(each_pos[0]) + int(each_pos[1]) + int(each_pos[2]) + int(each_pos[3])
    a = int(each_pos[0])/float(total)
    g = int(each_pos[1])/float(total)
    c = int(each_pos[2])/float(total)
    t = int(each_pos[3])/float(total)
    a_data.append(a)
    g_data.append(g)
    c_data.append(c)
    t_data.append(t)
print len(test)

plt.plot(x, a_data, 'ro', x, g_data, 'bo', x, c_data, 'go', x, t_data, 'co')
#plt.axis([1200,1400,0,1])
#plt.show()
plt.savefig(sys.argv[3])
