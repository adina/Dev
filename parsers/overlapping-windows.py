import sys

d = {}
for line in open(sys.argv[1]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    identity = float(data[2])
    length = int(data[3])
    q_start = int(data[6])
    q_end = int(data[7])
    h_start = int(data[8])
    h_end = int(data[9])
    evalue = float(data[-2])
    q_start2, q_end2 = min(q_start, q_end), max(q_start, q_end)
    q_window = range(q_start2, q_end2)
    
    if d.has_key(query):
        inter = len([val for val in d[query] if val in q_window])
        if inter > 30:
            continue
        else:
            print line, 
            for x in range(q_start2, q_end2):
                d[query].append(x)
    else:
        print line,
        d[query] = q_window


