f=$1
echo '
#maximal read length
#max_rd_len=200
[LIB]
#average insert size
#avg_ins=200
#if sequence needs to be reversed 
reverse_seq=0
#in which part(s) the reads are used
asm_flags=1
#in which order the reads are used while scaffolding
#rank=1
#fastq file for read 1 
#q1=/path/**LIBNAMEA**/fastq_read_1.fq
#fastq file for read 2 always follows fastq file for read 1
#q2=/path/**LIBNAMEA**/fastq_read_2.fq
#fasta file for read 1 
#f1=/path/**LIBNAMEA**/fasta_read_1.fa
##fastq file for read 2 always follows fastq file for read 1
#f2=/path/**LIBNAMEA**/fasta_read_2.fa
#fastq file for single reads
#q=/mnt/scratch/howead/artifacts-paper-redo/alternative-assemblies/soap/simHChc_110.fna.ht.group0063.fa
#fasta file for single reads
f='$f.se'
#a single fasta file for paired reads
#p='$f.pe
