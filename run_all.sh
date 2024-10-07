#!/bin/bash

mkdir -p "./results/"
global_start=$(date +%s)

for source in basic vectorized blas
  do
  local_start=$(date +%s)
  "./build/benchmark-$source" > "./results/$source.csv"
  local_end=$(date +%s)
  local_time=$(( local_end - local_start ))
  global_time=$(( local_end - global_start ))
  printf "%s, runtime: %.1f, global timer: %.1f\n" $source $local_time $global_time
done

export OMP_PLACES=threads
export OMP_PROC_BIND=spread

for source in outer inner-reduction inner-thread-reuse inner-reduction
  do
  for t in 1 4 16 64
    do
    export OMP_NUM_THREADS=$t
    local_start=$(date +%s)
    "./build/benchmark-openmp-$source" > "./results/openmp-$source.csv"
    local_end=$(date +%s)
    local_time=$(( local_end - local_start ))
    global_time=$(( local_end - global_start ))
    echo "$source $t" 
    printf "%s %d, runtime: %.1f, global timer: %.1f\n" $source $t $local_time $global_time
  done
done