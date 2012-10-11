import csv
import sys, os.path
import matplotlib
#matplotlib.use('Cairo')
import pylab
from pylab import plot, savefig, hist, axis, xlabel, ylabel, title

filein = open(sys.argv[1], 'r')

reader = csv.reader(filein, delimiter=' ')

xdata = []
ydata = []

list = []

for n, row in enumerate(reader):
    value = float(row[0])
    xdata.append(n)
    ydata.append(value)

plot(xdata, ydata)

#xlabel('')
#ylabel('')
#title('Distribution of Standard Deviation of Coverage')

savefig(sys.argv[2]+'.png')
