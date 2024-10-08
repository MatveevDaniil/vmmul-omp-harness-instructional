import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def mflop(n: int, method: str, num_thread: int) -> int:
  if method == 'blas' or method == 'outer':
    return 2 * n ** 2 + n
  elif method == 'inner':
    return 2 * n ** 2 + n + num_thread * n
  elif method == 'inner-thread-reuse':
    return 2 * n ** 2 + num_thread * n

def plot_mflop(res_name: str):
  if res_name == 'blas':
    method, num_thread = 'blas', None
  else:
    method = '-'.join(res_name.split('-')[1:-1])
    num_thread = int(res_name.split('-')[-1])
  df = pd.read_csv(f"results/{res_name}.csv")
  df = df.set_axis(['n', 'Time'], axis=1)
  df = df.drop(0)
  mflops = df['n'].apply(lambda i: mflop(i, method, num_thread)) / df['Time'] / 10 ** 6
  color = method2colors[res_name]
  plt.scatter(df['n'], mflops, label=res_name, s=10, marker='^', color=color)
  plt.plot(df['n'], mflops, color=color)

for method in 'inner', 'outer', 'inner-thread-reuse':
  method2colors = {
    'blas': 'black',
    f'openmp-{method}-1': 'red',
    f'openmp-{method}-4': 'green',
    f'openmp-{method}-16': 'blue',
    f'openmp-{method}-64': 'orange'
  }
  for res_type in method2colors:
    plot_mflop(res_type)


  plt.xlabel("n (vector size)")
  plt.ylabel('MFLOP/s')
  plt.title(f'MFLOP/s of paralle-{method} VMM vs CBLAS')
  plt.legend()
  plt.savefig(f'visualization_scripts/{method}.png', dpi=300)
  plt.clf()