#!/bin/bash
a=4.08     # Lattice parameter of gold (Au)
Lx=40.8 
Ly=20.4
Lz=20.4
VACOVP=0.76  # This paremeter must be set for each case. .76 is good for FCC
PBC="true"
Struc="FCC"

p=0
for file in ~/practica1/Vacancies/Au-fcc-10-5-5/*
do
	let p=p+1
	#echo "$p"
	#less $file >> prueba$p.txt
	../../saf/searchfill $file $VACOVP -L $Lx $Ly $Lz -a $a --struct $Struc --pbc $PBC | tail -n 1 >>Output_vacancies_file.txt
done 

#date
#echo ""
#echo "############################################################"
#../searchfill $1 $VACOVP -L $Lx $Ly $Lz -a $a --struct $Struc --pbc $PBC
#echo "############################################################"
#echo ""
#date
