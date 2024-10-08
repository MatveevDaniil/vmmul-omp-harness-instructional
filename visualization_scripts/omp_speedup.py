import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


basic_df = pd.read_csv(f"results/basic.csv")
basic_df = basic_df.set_axis(['n', 'Time'], axis=1)
basic_df = basic_df.drop(0)

def plot_mflop(res_name: str):
  if res_name == 'blas':
    method, num_thread = 'blas', None
  else:
    method = '-'.join(res_name.split('-')[1:-1])
    num_thread = int(res_name.split('-')[-1])
  df = pd.read_csv(f"results/{res_name}.csv")
  df = df.set_axis(['n', 'Time'], axis=1)
  df = df.drop(0)
  speedup = basic_df['Time'] / df['Time']
  color = method2colors[res_name]
  plt.scatter(df['n'], speedup, label=res_name, s=10, marker='^', color=color)
  plt.plot(df['n'], speedup, color=color)

for method in 'inner', 'outer', 'inner-thread-reuse':
  method2colors = {
    f'openmp-{method}-1': 'red',
    f'openmp-{method}-4': 'green',
    f'openmp-{method}-16': 'blue',
    f'openmp-{method}-64': 'orange'
  }
  for res_type in method2colors:
    plot_mflop(res_type)


  plt.xlabel("n (vector size)")
  plt.ylabel('Speedup')
  plt.title(f'Speedup of parallel-{method} VMMul over basic impl.')
  plt.legend()
  plt.savefig(f'visualization_scripts/{method}_speedup.png', dpi=300)
  plt.clf()