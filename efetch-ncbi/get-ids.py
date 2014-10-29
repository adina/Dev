#!/usr/bin/python

"""Download infomration on 'water pathogen' search query in NCBI

Command-line application that does a search and return (Adina Howe, 2014).
"""

from Bio import Entrez

Entrez.email = 'adina@iastate.edu'
handle = Entrez.esearch(db="genome", term="water pathogen", retmax=200)
records = Entrez.read(handle)


for i in records['IdList']:
    fp1 = open(i + '.summary', 'w')
    fp2 = open(i + '.links', 'w')

    handle1 = Entrez.esummary(db="genome", id=i)
    records1 = Entrez.read(handle1)
    print i
    fp1.write('%s\t%s\t%s\n' % (i, records1[0]['Organism_Name'], records1[0]['DefLine']))
    handle2 = Entrez.elink(dbfrom="genome", db="nucleotide", id=i)
    records2 = Entrez.read(handle2)
    fp2.write('%s\t' % i)
    list_of_dict_ids = records2[0]['LinkSetDb'][0]['Link']
    for link_id in list_of_dict_ids:
        fp2.write('%s\t' % link_id['Id'])
    fp2.write('\n')
