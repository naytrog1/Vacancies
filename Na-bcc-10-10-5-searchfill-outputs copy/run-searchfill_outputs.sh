#!/bin/bash
#SBATCH --job-name=nay
#SBATCH --partition=gpu
#SBATCH -n 1
#SBATCH --output=nay_%j.out
#SBATCH --error=nay_%j.error
#SBATCH --mail-user=fabian.gomez.ingfis@gmail.com
#SBATCH --mail-type=ALL


a=4.29       # Lattice parameter of gold (Au)
Lx=42.9 
Ly=42.9
Lz=21.45
VACOVP=0.26  # This paremeter must be set for each case. .76 is good for FCC
PBC="true"
Struc="BCC"

p=0
for file in ~/Vacancies/Na-bcc-10-10-5/*
do
	let p=p+1
	echo "$p"
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
