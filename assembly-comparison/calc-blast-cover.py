#! /usr/bin/env python
import sys
import blastparser
import screed


MIN_SCORE=200

covs = {}
for record in screed.open(sys.argv[1]):
    covs[record.name] = [0] * len(record.sequence)

#print 'before'
for record in blastparser.parse_fp(open(sys.argv[2])):
    #print record
    #print 'test'
    #sys.stdout.write('.')
    #sys.stdout.flush()

    #print record
    for hit in record.hits:
        #print hit
        for match in hit.matches:
            

            cov = covs[hit.subject_name]
            start = min(match.subject_start, match.subject_end) - 1
            end = max(match.subject_start, match.subject_end)
            for i in range(start, end):
                cov[i] = 1

print ''


coved = 0
total = 0
for name in covs:
    if len(covs[name]) < MIN_SCORE:
        continue

    coved += sum(covs[name])
    total += len(covs[name])
    f = sum(covs[name]) / float(len(covs[name]))
    print name, sum(covs[name]), len(covs[name]), f


print coved, total, coved / float(total)
