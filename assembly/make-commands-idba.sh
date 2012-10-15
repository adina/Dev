for f in *fa;
do 
echo '/mnt/home/howead/software/idba-0.18/bin/idba -r' $f '-o' $f.idba '--mink 25 --maxk 50 --minCount 0'
done