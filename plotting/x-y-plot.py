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
    xdata.append(int(row[0]))
    ydata.append(float(row[1]))

plot(xdata, ydata)

xlabel('Contig Length')
ylabel('Fraction bp that are stoptags')
#title('Does stoptag usage change with length of contig?')

savefig(sys.argv[2]+'.png')
