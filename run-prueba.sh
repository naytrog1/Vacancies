#!/bin/bash
array=( "Au 1. 2. 3." "Au 4. 5. 6." "Fe 7. 8. 9." "Fe 10. 11. 12." )
function join_by { local d=$1;shift; echo -n  -p "$1"; shift; printf "%s" "${@/#/$d}"; }
a=$(join_by ' -p ' "${array[@]}")
echo ""
echo nice
./prueba.py $a
echo done
