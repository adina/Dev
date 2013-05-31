ls *raw*raw*txt
ls *raw*knot*txt
ls *knot*knot*.txt
ls *knot*raw*txt

python ~/Dev/assembly-comparison/normize.py *raw*raw*txt *raw*knot*txt > raw-knot.txt
python ~/Dev/assembly-comparison/normize.py *knot*knot*txt *knot*raw*txt > knot-raw.txt
