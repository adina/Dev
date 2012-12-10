for f in *group*ass*35;do for g in ${f%.ass*};
 
    do for each_file in $g*ass*;


     do echo $each_file;
      cat $each_file/contigs.fa >> $g-combined-contigs.fa;
      done;
    done;

done