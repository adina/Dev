import os, sys, glob, screed

#python rename-contigs-groupid.py *ass*

'''generates new names for contigs containing groupids'''

list_assemblies = glob.glob('*ass*')

for x in list_assemblies:
    contig_file = x + '/contigs.fa'
    groupid = x.split('group')[1].split('.fa')[0]
    fp = open(contig_file + '.renamed', 'w')
    for record in screed.open(contig_file):
        print >> fp, '>group' + groupid + '_' + record.name
        print >> fp, record.sequence
    fp.close()
