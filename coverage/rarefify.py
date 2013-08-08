import sys, random

bins = [10e3, 10e4, 1e6, 5e6, 1e7, 5e7, 1e8]
#bins = [1, 2, 3, 4, 5, 6, 10]

l = []
d1 = {}
d2 = {}
d3 = {}
d4 = {}
d5 = {}
d6 = {}
d7 = {}

for n, line in enumerate(open(sys.argv[1])):
      l.append(line.rstrip())

random_l = random.sample(l, int(bins[-1]))

for n, item in enumerate(random_l):
    if n < bins[0]:
          d1[item] = ''
    if n >= bins[0] and n < bins[1]:
          d2[item] = ''
    if n >= bins[1] and n < bins[2]:
          d3[item] = ''
    if n >= bins[2] and n < bins[3]:
          d4[item] = ''
    if n >= bins[3] and n <= bins[4]:
          d5[item] = ''
    if n >= bins[4] and n <= bins[5]:
          d6[item] = ''
    if n >= bins[5] and n <= bins[6]:
          d7[item] = ''

name_id = sys.argv[2] + '.' + sys.argv[3]

fp1 = open(name_id + '.' + "1", 'w') #10000
fp2 = open(name_id + '.' + "2", 'w') #100000
fp3 = open(name_id + '.' + "3", 'w') #1e6
fp4 = open(name_id + '.' + "4", 'w') #5e6
fp5 = open(name_id + '.' + "5", 'w') #5e6
fp6 = open(name_id + '.' + "6", 'w') #5e6
fp7 = open(name_id + '.' + "7", 'w') #5e6

for m, line in enumerate(open(sys.argv[2])):
    dat = line.rstrip().split('\t')[0]
    if dat in d1:
          fp1.write('%s' % line)
    elif dat in d2:
          fp2.write('%s' % line)
    elif dat in d3:
          fp3.write('%s' % line)
    elif dat in d4:
          fp4.write('%s' % line)
    elif dat in d5:
          fp5.write('%s' % line)
    elif dat in d6:
          fp6.write('%s' % line)
    elif dat in d7:
          fp7.write('%s' % line)
    else:
          continue
