import sys

#    print key, median, avg, minl, maxl, summy, total, cov_rat
count_ok = 0
fp = open(sys.argv[2], 'w')
for n, line in enumerate(open(sys.argv[1])):
    key, median, avg, minl, maxl, summy, total, cov_rat = line.rstrip().split(' ')

    if int(maxl) >= 2:
        if int(summy) >= 100:
            fp.write('%s' % line)
            count_ok += 1

total_hits = n + 1
total_passed = count_ok
total_perc = float(count_ok) / float(n+1)

print 'Total hits:', total_hits
print 'Pass filter:', total_passed, total_perc
