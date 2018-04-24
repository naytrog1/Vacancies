#!/bin/bash
Element="Au"
Type="fcc"
Constant=4.08
NX=10
NY=10
NZ=20
PV=25.0

date
echo ""
echo "############################################################"
./Lattices.py -e $Element -t $Type -a $Constant -nx $NX -ny $NY -nz $NZ -v $PV
echo "############################################################"
echo ""
date
