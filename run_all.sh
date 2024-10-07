#!/bin/bash

mkdir -p "./results/"

for source in basic vectorized blas
  do
  "./build/benchmark-$source" > "./results/$source.csv"
done

export OMP_PLACES=threads
export OMP_PROC_BIND=spread

# inner inner-thread-reuse inner-reduction
for source in outer inner-reduction
  do
  for t in 1 4 16 64
    do
    export OMP_NUM_THREADS=$t
    echo "$source $t" 
    "./build/benchmark-openmp-$source" > "./results/openmp-$source.csv"
  done
done