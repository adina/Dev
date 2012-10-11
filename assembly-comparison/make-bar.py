import matplotlib.pyplot as plt
import sys
import numpy as np

x = []
y1 = []
y2 = []
y3 = []

def get_data(file):
    x = []
    y1 = []
    y2 = []
    y3 =[]
    for n, line in enumerate(file):
        line = line.rstrip().split(' ')
        x.append(line[0])
        y1.append(int(line[1]))
        y2.append(int(line[2])+y1[n])
        y3.append(int(line[3])+y1[n]+y2[n])
    return(x, y1, y2, y3)

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

xa, y1a, y2a, y3a = get_data(file1)
xb, y1b, y2b, y3b = get_data(file2)

print xa
Na = len(xa)
print Na
inda = np.arange(Na)
widtha = 0.3

plt.subplot(111)

rects1 = plt.bar(inda, y1a, widtha, color='r', hatch='\\') + plt.bar(inda, y2a, widtha, bottom=y1a, color='y', hatch='\\') + plt.bar(inda, y3a, widtha, bottom=y2a, color='g', hatch='\\') + plt.bar(inda+widtha, y1b, widtha, color='r') + plt.bar(inda+widtha, y2b, widtha, bottom=y1b, color='y') + plt.bar(inda+widtha, y3b, widtha, bottom=y2b, color='g')

plt.xticks(inda+widtha, xa, rotation='vertical', fontsize='xx-small')
#plt.show()
plt.savefig('contig-lengths.pdf')
