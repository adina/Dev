import sys
import os
import json
import urllib
import subprocess

def taxid_to_taxonomy(taxid):
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=" + taxid + "&retmode=xml"
    proc = subprocess.Popen(["curl", url], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    l = []
    for line in out.split('\n'):
        if line.strip().startswith("<ScientificName>"):
            dat = line.strip().split('<ScientificName>')[1].split('</ScientificName>')[0]
            l.append(dat)
    taxonomy = ';'.join(l)
    return(taxonomy)

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        dat = line.rstrip().split('\t')
        taxa = taxid_to_taxonomy(dat[1])
        taxa = taxa.split(';')
        print dat[0] + '\t' + '\t'.join(taxa)
    

