import sys, screed
import matplotlib
matplotlib.use('Agg')
import pylab
import matplotlib.pyplot as plt


list = []
list2 = []
for line in open(sys.argv[1]):
    line = float(line.rstrip().split(' ')[1])
    list.append(line)
for line in open(sys.argv[2]):
    line = float(line.rstrip().split(' ')[1])
    list2.append(line)


fig = plt.figure()

ax = fig.add_subplot(211)
ax.hist(list, 2200, cumulative=False, normed=True, alpha=0.8, color='g')
ax.set_xlim(0,50)
ax.set_ylim(0,0.10)
ax.set_ylabel('Relative abundance')

ax2 = fig.add_subplot(212)
ax2.hist(list2, 1450, cumulative=False, normed=True, alpha=0.8, color='m')
ax2.set_xlim(0,50)
ax2.set_ylim(0,0.10)
ax2.set_xlabel('Median basepair coverage of assembled contigs')
ax2.set_ylabel('Relative abundance')
#plt.axis([0,50,0,0.10])
#plt.title(sys.argv[1] + ' Assembly Coverage Distribution')

plt.savefig('fig3-coverage.eps', dpi=300)



