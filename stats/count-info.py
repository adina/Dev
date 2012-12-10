import sys, screed

count_bp = 0
count_read = 0

for n, record in enumerate(screed.open(sys.argv[1])):
    count_read += 1
    for x in record.sequence:
        count_bp += 1

print sys.argv[1], 'bp=', '\t', count_bp, '\t', 'reads=', '\t', count_read
