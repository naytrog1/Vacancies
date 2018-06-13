#!/bin/bash
Element="Na"
Type="bcc"
Constant=4.29
NX=10
NY=10
NZ=5
Ouputs=1
PV=25.0

date
./Lattices_copy.py -e $Element -t $Type -a $Constant -nx $NX -ny $NY -nz $NZ -o $Ouputs -v $PV
echo "Saved $Ouputs Ouputs."
date
