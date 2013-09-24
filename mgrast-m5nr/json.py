import os
import json
import urllib

for line in open("foo.txt", 'rU'):
    d = json.loads(line)

print d.keys()
print d[u'data']
