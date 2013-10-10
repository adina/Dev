import sys

l = []
for line in open(sys.argv[1]):
    dat = line.rstrip()
    l.append(dat)

l_index = []
for i in range(0, len(l)+1, 2):
    l_index.append(i)

step = 0
count = 2
for ind in l_index:
    try:
        int(l[(ind-step)])
        snip = l[(ind-step):(ind-step+count)]
        print snip[0], '\t', snip[1]
    except:
        #print step
        step = step + 1
        snip =  l[(ind-step):(ind-step+count)]
        print snip[0], '\t', snip[1]
        #print step
