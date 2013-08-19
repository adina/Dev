import sys 
from Bio import SeqIO

genome=SeqIO.read(sys.argv[1], 'genbank')

print genome.annotations['source'], '\t', ';'.join(genome.annotations['taxonomy'])


#for feat in genome.features:
    
    #if feat.type == 'source':
    #    print feat
    
        
        #print sys.argv[1].split('.')[0], '\t', feat.qualifiers['organism'][0], '\t', feat.qualifiers['db_xref'][0]
