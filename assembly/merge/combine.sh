for f in *group*ass*35;
do for g in ${f%.ass*};
 
    do for each_file in $g*ass*;


     do echo $each_file;
      cat $each_file/contigs.fa >> $g-combined-contigs.fa;
      done;
    done;
done

for x in *combined-contigs.fa; do python rename-for-minimus.py $x > $x.renamed; done

