import sys, random

d = {}
for line in open(sys.argv[1]):
    l1, l2, l3, l4, l5, l6, l7 = line.rstrip().split('\t')
    d[l7] = (l1, l2, l3, l4, l5, l6)

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
            if ssid == "Flavobacterium johnsonia johnsoniae UW101":
                ssid = "Flavobacterium johnsoniae UW101"
            if ssid == "Mycobacterium vanbaaleni vanbaalenii PYR-1":
                ssid = "Mycobacterium vanbaalenii PYR-1"
            if ssid == "Alkaliphilus oremlandi oremlandii OhILAs":
                ssid = "Alkaliphilus oremlandii OhILAs"
            if ssid == "Roseiflexus castenholzi DSM 13941":
                ssid = "Roseiflexus castenholzii DSM 13941"
            if ssid == "Sanguibacter keddiei keddieii DSM 10542":
                ssid = "Sanguibacter keddieii DSM 10542"
            if ssid == "Cyanothece sp PCC 7424":
                ssid = "Cyanothece sp. PCC 7424"
            if ssid == "Leptothrix cholodni SP-6":
                ssid = "Leptothrix cholodnii SP-6"
            if ssid == "Bacillus B-14905":
                ssid = "Bacillus sp. B14905"
            if ssid == "Psychromonas ingrahami ingrahamii 37":
                ssid = "Psychromonas ingrahamii 37"
            l = [contig, ssid, d[ssid][0], d[ssid][1], d[ssid][2]]
            print '\t'.join(l)

