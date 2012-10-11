import csv
import sys, os.path
import matplotlib
#matplotlib.use('Cairo')
import pylab
from pylab import plot, savefig, hist, axis, xlabel, ylabel, title

filein = open(sys.argv[1], 'r')

n_bins = 100

reader = csv.reader(filein, delimiter=' ')

#xdata = []
#ydata = []

list = []

for row in reader:
    value = float(row[0])
    list.append(value)

hist(list, n_bins, cumulative=False, normed=False, alpha=0.8)

#axis([0,50,0,1e7])

#xlabel('')
#ylabel('')
#title('Distribution of Standard Deviation of Coverage')

savefig(sys.argv[2]+'.png')
