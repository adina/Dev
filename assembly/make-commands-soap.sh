for f in *fa;
do 

base=`basename $f`
echo 'SOAPdenovo-31mer all -K 31 -p 8 -o' $f-soap '-s '$base.config
done