#!/usr/bin/python

"""Download genomes from NCBI

Command-line application that does a search and return (Adina Howe, 2014).
"""
import sys
from Bio import Entrez, SeqIO

l = []
for line in open(sys.argv[1]):
    dat = line.rstrip().split('\t')
    for x in dat:
        l.append(dat[1:])

for sequence_id in l:
    Entrez.email = 'adina@iastate.edu'
    handle = Entrez.efetch(db="nuccore", id=sequence_id, rettype="gb", retmode="xml")
    for x in handle:
        print x
    
    '''
    for record in SeqIO.parse(handle, "fasta"):
        print record
        print '-----'
    print 'xxxxxxxx'
    '''
