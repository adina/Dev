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
    hist_list.append(x[1])

fig = plt.figure()
ax = fig.add_subplot(111)
n, bins, patches = ax.hist(hist_list, 300, cumulative=False, normed=False, alpha=0.8)

plt.xlabel('Contig Length - bp')
plt.ylabel('# of Contigs with Specified Length')
plt.axis([0,5000,0,50000])
plt.title(sys.argv[1] + ' Assembly Length Distribution')
#plt.show()
plt.savefig(sys.argv[1] + '.length.pdf')



