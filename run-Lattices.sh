#!/bin/bash
a = 1      # Lattice parameter of gold (Au)
Element="Au"
Struct="fcc" 
NX= 2 
NY= 2
NZ= 1

PBC="true"
Struc="FCC"

if [ "$1" == "" ]; then
 echo "USAGE:"
 echo "     ./run-searchfill  input-file.xyz"
 exit
fi

date
echo ""
echo "############################################################"
../searchfill $1 -e $Element -t $Type -a $a -nx $NX -ny $NY -nz $NZ -v $PV
echo "############################################################"
echo ""
date
