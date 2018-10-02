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
VACOVP=0.16  # This paremeter must be set for each case. .76 is good for FCC
PBC="fase"
Struc="FCC"

if [ "$1" == "" ]; then
 echo "USAGE:"
 echo "     ./run-searchfill_outputs.sh  input-file.xyz"
 exit
fi

date
echo ""
echo "############################################################"
../saf/searchfill $1 $VACOVP -L $Lx $Ly $Lz -a $a --struct $Struc --pbc $PBC
echo "############################################################"
echo ""
date
