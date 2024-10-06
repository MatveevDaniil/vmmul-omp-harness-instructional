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
/*
  https://www.openmp.org/spec-html/5.0/openmpsu41.html#x62-1040002.9
  "When no chunk_size is specified, the iteration space is divided into chunks that are approximately equal in size, and at most one chunk is distributed to each thread. "

*/

void my_dgemv(int n, double* A, double* x, double* y) {
  #pragma omp parallel for
  for (int j = 0; j < n; j++)
    for (int i = 0; i < n; i++)
      #pragma omp atomic
      y[i] += A[i * n + j] * x[j];
}

