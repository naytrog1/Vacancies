#!/bin/bash
Element="Au"
Type="fcc"
Constant=1
NX=1 
NY=1
NZ=1
PV=50.0

if [ "$1" == "" ]; then
 echo "USAGE:"
 echo "     ./run-Lattices"
 exit
fi

date
echo ""
echo "############################################################"
./Lattices $1 -e $Element -t $Type -a $Constant -nx $NX -ny $NY -nz $NZ -v $PV
echo "############################################################"
echo ""
date
