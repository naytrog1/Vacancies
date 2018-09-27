#!/bin/bash
#SBATCH --job-name=nay
#SBATCH --partition=gpu
#SBATCH -n 1
#SBATCH --output=nay_%j.out
#SBATCH --error=nay_%j.error
#SBATCH --mail-user=fabian.gomez.ingfis@gmail.com
#SBATCH --mail-type=ALL


a=5.62       # Lattice parameter of gold (Au)
Lx=11.24
Ly=11.24
Lz=11.24
VACOVP=0.76  # This paremeter must be set for each case. .76 is good for FCC
PBC="false"
Struc="FCC"

if [ "$1" == "" ]; then
 echo "USAGE:"
 echo "     ./run-searchfill  input-file.xyz"
 exit
fi

date
echo ""
echo "############################################################"
../saf/searchfill NaCl_2-2-2_Vacancies.xyz $VACOVP -L $Lx $Ly $Lz -a $a --struct $Struc --pbc $PBC
echo "############################################################"
echo ""
date
