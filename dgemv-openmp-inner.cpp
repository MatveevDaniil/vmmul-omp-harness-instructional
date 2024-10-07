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
  for (int i = 0; i < n; i++) {
    double sum = 0;
    #pragma omp parallel 
    {
      double thread_sum = 0;
      #pragma omp for
      for (int j = 0; j < n; j++)
        thread_sum += A[i * n + j] * x[j];
      #pragma omp atomic
      sum += thread_sum;
    }
    y[i] += sum;
  }
}

