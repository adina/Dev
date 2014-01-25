import sys, random

d = {}
for line in open(sys.argv[1]):
    ssid, l1, l2, l3 = line.rstrip().split('\t')
    d[ssid] = (l1, l2, l3)

fp = open(sys.argv[2] + '.duplicates.txt', 'w')
for n, line in enumerate(open(sys.argv[2])):
    if n > 0:
        if line.startswith('Download'):
            continue
        else:
            dat = line.rstrip().split('\t')
            contig = dat[0].split('|')[1]
            ssid_list = dat[-1].split(';')
            if len(ssid_list) > 1:
                ssid = random.choice(ssid_list)
                fp.write('%s\t' % contig)
                fp.write('%s\n' % ';'.join(ssid_list))
            else:
                ssid = ssid_list[0]
            l = [contig, ssid, d[ssid][0], d[ssid][1], d[ssid][2]]
            print '\t'.join(l)
