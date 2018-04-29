#!/bin/bash
a=3.51       # Lattice parameter of gold (Au)
Lx=7.02 
Ly=7.02
Lz=7.02 
VACOVP=0.16  # This paremeter must be set for each case. .76 is good for FCC
PBC="true"
Struc="BCC"

p=0
for file in ~/practica1/Vacancies/Li-bcc/*
do
	let p=p+1
	#echo "$p"
	#less $file >> prueba$p.txt
	../../saf/searchfill $file $VACOVP -L $Lx $Ly $Lz -a $a --struct $Struc --pbc $PBC >>Output_vacancies_file_"$p".txt
done 

#date
#echo ""
#echo "############################################################"
#../searchfill $1 $VACOVP -L $Lx $Ly $Lz -a $a --struct $Struc --pbc $PBC
#echo "############################################################"
#echo ""
#date