#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

const char* dgemv_desc = "OpenMP dgemv.";

void my_dgemv(int n, double* A, double* x, double* y) {
  #pragma omp parallel 
  {
    int thread_range = n / omp_get_num_threads();
    int thread_id = omp_get_thread_num();
    int start = thread_id * thread_range;
    int end = start + thread_range;
    for (int i = 0; i < n; i++)
      for (int j = start; j < end; j++)
        #pragma omp atomic
        y[i] += A[i * n + j] * x[j];
  }
}

