#!/usr/bin/python

"""Download genomes from NCBI

Command-line application that does a search and return (Adina Howe, 2014).
"""
import sys
from Bio import Entrez, SeqIO

l = []
for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    l.append(dat)

fp = open(sys.argv[2], 'w')

for sequence_id in l:
    Entrez.email = 'adina@iastate.edu'
    handle = Entrez.efetch(db="protein", id=sequence_id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, 'genbank')
    for feat in record.features:
        if feat.type == "source":
            fp.write('%s\t%s\t' % (sequence_id, feat.qualifiers['organism'][0]))
            for n, each in enumerate(feat.qualifiers['db_xref']):
                if feat.qualifiers['db_xref'][n].startswith('taxon'):
                    taxid = feat.qualifiers['db_xref'][n].split(':')[1]
            handle2 = Entrez.efetch(db="taxonomy", id = taxid, retmode="xml")
            record = Entrez.parse(handle2, "seqxml")
            for x in record:
                fp.write('%s\t\n' % x['Lineage'])


        

