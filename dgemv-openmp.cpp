#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

const char* dgemv_desc = "OpenMP dgemv.";

/*
 * This routine performs a dgemv operation
 * Y :=  A * X + Y
 * where A is n-by-n matrix stored in row-major format, and X and Y are n by 1 vectors.
 * On exit, A and X maintain their input values.
 */

void my_dgemv(int n, double* A, double* x, double* y) {

  #pragma omp parallel
  {
    int thread_range = n / omp_get_num_threads();
    int thread_id = omp_get_thread_num();
    int start = thread_id * thread_range;
    int end = start + thread_range;
    for (int i = start; i < end; i++)
      for (int j = 0; j < end; j++)
        y[i] += A[i * n + j] * x[j];
  }
}

