import sys, screed
import matplotlib
matplotlib.use('Agg')
import pylab
import matplotlib.pyplot as plt


list = []
for record in screed.open(sys.argv[1]):
    cov = float(record.name.split('cov=')[1][:-1])
    length = len(record.sequence)
    data = (cov, length)
    list.append(data)

#histogram of coverage distribution
hist_list = []

for x in list:
    hist_list.append(x[0])

fig = plt.figure()
ax = fig.add_subplot(111)
n, bins, patches = ax.hist(hist_list, 300, cumulative=False, normed=False, alpha=0.8)

plt.xlabel('Contig Coverage - Median bp')
plt.ylabel('# of Contigs with Specified Coverage')
plt.axis([0,100,0,300000])
plt.title(sys.argv[1] + ' Assembly Coverage Distribution')
#plt.show()
plt.savefig(sys.argv[1] + '.coverage.pdf')



