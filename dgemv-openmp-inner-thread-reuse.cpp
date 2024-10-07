#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

const char* dgemv_desc = "OpenMP dgemv.";

void my_dgemv(int n, double* A, double* x, double* y) {
  #pragma omp parallel 
  {
    for (int i = 0; i < n; i++)
    #pragma omp parallel for
    for (int j = 0; j < n; j++)
      #pragma omp atomic
      y[i] += A[i * n + j] * x[j];
  }
}

