#!/bin/bash
#SBATCH --job-name=prueba
#SBATCH --partition=gpu
#SBATCH -n 1
#SBATCH --output=prueba_%j.out
#SBATCH --error=prueba_%j.error
#SBATCH --mail-user=fabian.gomez.ingifs@gmail.com
#SBATCH --mail-type=ALL

./run-searchfill_outputs.sh
