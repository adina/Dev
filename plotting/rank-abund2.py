import csv
import sys, os.path
import matplotlib
#matplotlib.use('Cairo')
import pylab
from pylab import plot, savefig, hist, axis, xlabel, ylabel, title

filein = open(sys.argv[1], 'r')
filein2 = open(sys.argv[2], 'r')

reader = csv.reader(filein, delimiter=' ')
reader2 = csv.reader(filein2, delimiter=' ')

xdata = []
ydata = []
xdata2 = []
ydata2 = []


for n, row in enumerate(reader):
    value = float(row[0])
    xdata.append(n)
    ydata.append(value)

for n, row in enumerate(reader2):
    value = float(row[0])
    xdata2.append(n)
    ydata2.append(value)

plot(xdata, ydata, 'ro', xdata2, ydata2, 'bx')

#xlabel('')
#ylabel('')
#title('Distribution of Standard Deviation of Coverage')

savefig(sys.argv[3]+'.png')
