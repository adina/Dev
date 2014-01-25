import os
import json
import urllib
import sys
import subprocess

proc = subprocess.Popen(["curl", "http://kbase.us/services/communities/1/m5nr/ontology?source=Subsystems&min_level=function&version=1"], stdout=subprocess.PIPE)
(out, err) = proc.communicate()

d = json.loads(out)
for x in d['data']:
    if x.has_key('level2'):
        l = [x['accession'], x['level3'], x['level2'], x['level1']]
    else:
        x['level2'] = "NA"
        l = [x['accession'], x['level3'], x['level2'], x['level1']]

    print '\t'.join(l)

