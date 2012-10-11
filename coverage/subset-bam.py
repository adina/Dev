import pysam, sys

samfile = pysam.Samfile(sys.argv[1], 'rb')
subset = pysam.Samfile(sys.argv[1]+'.'+sys.argv[2], 'wb', template=samfile)

for read in samfile.fetch():
    contig_id = samfile.getrname(read.rname)
    contig_len = int(contig_id.split(' ')[0].rsplit('.',1)[1])
    if contig_len > int(sys.argv[2]):
        subset.write(read)
