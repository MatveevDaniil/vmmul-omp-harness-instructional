const char* dgemv_desc = "Basic implementation of matrix-vector multiply.";

void my_dgemv(int n, double* A, double* x, double* y) {
  for (int i = 0; i < n; i++) {
    double sum = 0;
    for (int j = 0; j < n; j++)
      sum += A[i * n + j] * x[j];
    y[i] += sum;
  }
}
