import screed, sys

l = []
for record in screed.open(sys.argv[1]):
    l.append(len(record.sequence))

print max(l)
print min(l)

