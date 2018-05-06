#!/bin/bash
Element="Au"
Type="fcc"
Constant=4.08
NX=10
NY=5
NZ=5
Ouputs=1000
PV=25.0

date
./Lattices_copy.py -e $Element -t $Type -a $Constant -nx $NX -ny $NY -nz $NZ -o $Ouputs -v $PV
echo "Saved $Ouputs Ouputs."
date
