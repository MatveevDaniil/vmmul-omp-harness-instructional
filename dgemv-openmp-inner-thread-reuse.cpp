#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

const char* dgemv_desc = "OpenMP dgemv.";

void my_dgemv(int n, double* A, double* x, double* y) {
  #pragma omp parallel 
  {
    for (int i = 0; i < n; i++) {
      double thread_sum = 0;
      #pragma omp for
      for (int j = 0; j < n; j++)
        thread_sum += A[i * n + j] * x[j];
      #pragma omp atomic
      y[i] += thread_sum;
    }
  }
}

