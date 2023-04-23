import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
path = f'results/{sys.argv[1]}.csv'
header = ['8', '16', '32', '64', '128', '256', '512']
df = pd.read_csv(path, names = header)
n = df.shape[0]
colors = plt.cm.rainbow(np.linspace(0, 1, n))

for i in range(df.shape[0]):
    y = df.iloc[i, :]
    plt.plot(header, y, '-o', color=colors[i])

#show legend in the plot
plt.legend(['PSO', 'Greedy', 'Genetic Algorithm', 'Dynamic Programmng', 'Divide and Conquer', 'Simulated Annealing'], loc='upper left')
plt.show()


