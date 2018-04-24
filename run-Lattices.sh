#!/bin/bash
Element="Au"
Type="fcc"
Constant=1
NX=1 
NY=1
NZ=1
PV=25.0

date
echo ""
echo "############################################################"
./Lattices.py -e $Element -t $Type -a $Constant -nx $NX -ny $NY -nz $NZ -v $PV
echo "############################################################"
echo ""
date
