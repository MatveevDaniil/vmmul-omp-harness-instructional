import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def mflop(n: int) -> int:
  return 2 * n ** 2 + n
# '#E41A1C', '#377EB8', '#4DAF4A'
method2colors = {
  'basic': 'red', 
  'vectorized': 'blue', 
  'blas': 'black'
}

def plot_mflop(res_name: str):
  df = pd.read_csv(f"results/{res_name}.csv")
  df = df.set_axis(['n', 'Time'], axis=1)
  df = df.drop(0)
  mflop = df['n'].apply(mflop)
  mflops = mflop / df['Time'] / 10 ** 6
  color = method2colors[res_name]
  plt.scatter(df['n'], mflops, label=res_name, s=10, marker='^', color=color)
  plt.plot(df['n'], mflops, color=color)

for res_type in method2colors:
  plot_mflop(res_type)


plt.xlabel("n (vector size)")
plt.ylabel('MFLOP/s')
plt.title('MFLOP/s of non-parallel implementations of VMMul')
plt.legend()
plt.savefig(f'visualization_scripts/cblas_basic_vec.png', dpi=300)
plt.clf()