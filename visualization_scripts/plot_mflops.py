import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def mflop(n: int) -> int:
  return 2 * n ** 2

def plot_blas():
  df = pd.read_csv(f"results/blas.csv").drop(0)
  runtime = df['Time']
  mflops = df['n'].apply(mflop) / df['Time'] / 10 ** 6
  y_value = mflops if plot_mode == 'mflops' else runtime
  plt.scatter(df['n'], y_value, label=blas_benchmark, s=10, marker='^', color='red')
  plt.plot(df['n'], y_value, color='red')

def set_axes_and_save(fname: str, title: str):
  plt.xlabel("Matrix dimension")
  plt.ylabel(ylabel)
  plt.title(title)
  plt.legend()
  plt.savefig(f'visualization_scripts/{fname}.png', dpi=300)
  plt.clf()

for plot_mode in 'mflops', 'time':
  ### blas
  blas_benchmark = 'blas'
  ylabel = 'MFLOPs' if plot_mode == 'mflops' else 'Time (s)'

  ### basic
  basic_benchmarks = [f'basic-{benchmark}' for benchmark in ('ijk', 'ikj', 'jik', 'jki', 'kij', 'kji')]
  for benchmark in basic_benchmarks:
    df = pd.read_csv(f"results/{benchmark}.csv").drop(0)
    runtime = df['Time']
    mflops = df['n'].apply(mflop) / df['Time'] / 10 ** 6
    y_value = mflops if plot_mode == 'mflops' else runtime
    plt.scatter(df['n'], y_value, label=benchmark, s=10)
    plt.plot(df['n'], y_value)
  plot_blas()
  set_axes_and_save(f'basic_{plot_mode}', "Three-loop algorithms' performance")

  ### blocked
  blocked_benchmarks = ['blocked', 'blocked-templated']
  markers = {'blocked': 'o', 'blocked-templated': 's'}
  for benchmark in blocked_benchmarks:
    for block_size in 2, 16, 32, 64:
      df = pd.read_csv(f"results/{benchmark}.csv").drop([0, 1, 2, 3])
      df = df[df['Block Size'] == block_size] 
      runtime = df['Time']
      mflops = df['n'].apply(lambda n: mflop(n, block_size)) / df['Time'] / 10 ** 6
      y_value = mflops if plot_mode == 'mflops' else runtime
      plt.scatter(df['n'], y_value, label=f'{benchmark}-{block_size}', s=10, marker=markers[benchmark])
      plt.plot(df['n'], y_value)
  plot_blas()
  set_axes_and_save(f'blocked_{plot_mode}', "Fixed-block algorithms' performance")