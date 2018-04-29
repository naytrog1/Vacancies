#!/bin/bash
Element="Li"
Type="bcc"
Constant=3.51
NX=2
NY=2
NZ=2
Ouputs=2
PV=50.0

date
./Lattices_copy.py -e $Element -t $Type -a $Constant -nx $NX -ny $NY -nz $NZ -o $Ouputs -v $PV
echo "Saved $Ouputs Ouputs."
date