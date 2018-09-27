#!/bin/bash
array=( "Au 1. 2. 3." "Au 4. 5. 6." "Fe 7. 8. 9." "Fe 10. 11. 12." )
function join_by { local d=$1;shift; echo -n "$1"; shift; printf "%s" "${@/#/$d}"; }
Bases=$(join_by ' -eb ' "${array[@]}")
echo $Bases
Constant=4.29
NX=1
NY=1
NZ=1
Ouputs=1
PV=25.0

date
./Lattices_mix.py -eb $Bases -a $Constant -nx $NX -ny $NY -nz $NZ -o $Ouputs -v $PV
echo "Saved $Ouputs Ouputs."
date
