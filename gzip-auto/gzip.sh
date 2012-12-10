mkfifo file1.fifo
mkfifo file2.fifo
gunzip -c file1.gz > file1.fifo &
gunzip -c file2.gz > file2.fifo &