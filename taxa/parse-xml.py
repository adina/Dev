import sys
import json
import os
import urllib
import subprocess

t = []
for line in open(sys.argv[1]):
    dat = line.rstrip().split(' ')
    t.append(dat[1])

for x in t:
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=" + x + "&retmode=xml"
    proc = subprocess.Popen(["curl", url], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    l = []
    for line in out.split('\n'):
        if line.strip().startswith("<ScientificName>"):
            dat = line.strip().split('<ScientificName>')[1].split('</ScientificName>')[0]
            l.append(dat)
    l.insert(0, x)
    print '\t'.join(l)

