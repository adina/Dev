import os
import json
import urllib
import sys
import subprocess

#"version":"1","url":"http://kbase.us/services/communities/1/m5nr/taxonomy?min_level=species","data":[{"domain":"Eukaryota","order":"Passeriformes","genus":"Sporophila","class":"Aves","phylum":"Chordata","species":"Sporophila cinnamomea","ncbi_tax_id":0,"organism":"Sporophila cinnamomea (chestnut seedeater)","family":"Fringillidae"},{"domain":"Viruses","order":"unclassified (derived from Viruses)","genus":"Influenzavirus A","class":"unclassified (derived from Viruses)","phylum":"unclassified (derived from Viruses)","species":"Influenza A virus","ncbi_tax_id":672388,"organism":"Influenza A virus (A/Washington/19/2009(H3N2))","family":"Orthomyxoviridae"},{"domain":"Eukaryota","order":"Trichoptera","genus":"Ecnomus","class":"Insecta","phylum":"Arthropoda","species":"Ecnomus sp. EL3","ncbi_tax_id":623162,"organism":"Ecnomus sp. EL3","family":"Ecnomidae"},{"domain":"Viruses","order":"unclassified (derived from Viruses)","genus":"Norovirus","class":"unclassified (derived from Viruses)","phylum":"unclassified (derived from Viruses)","species":"Norwalk virus","ncbi_tax_id":534547,"organism":"Norovirus Hu/P3-20/2000/SWE","family":"Caliciviridae"},{"domain":"Eukaryota","order":"Cypriniformes","genus":"Pteronotropis","class":"Actinopterygii","phylum":"Chordata","species":"Pteronotropis hypselopterus","ncbi_tax_id":126325,"organism":"Pteronotropis hypselopterus","family":"Cyprinidae"},{"domain":"Eukaryota","order":"Squamata","genus":"Chelosania","class":"unc

#proc = subprocess.Popen(["curl", "http://kbase.us/services/communities/1/m5nr/taxonomy?&version=1"], stdout=subprocess.PIPE)

proc = subprocess.Popen(["curl", "http://kbase.us/services/communities/1/m5nr/taxonomy?&version=10&source=Subsystems"], stdout=subprocess.PIPE)
(out, err) = proc.communicate()

d = json.loads(out)
for x in d['data']:
    if x.has_key('species'):
        l = [x['domain'], x['order'], x['genus'], x['phylum'],x['class'],x['species'],x['organism']]
    print '\t'.join(l)

