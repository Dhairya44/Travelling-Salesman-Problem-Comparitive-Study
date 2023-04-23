import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
path = f'results/{sys.argv[1]}.csv'
df = pd.read_csv(path)

plt.plot(df.iloc[:, 0], df.iloc[:, 2],'-o', color='red')
plt.title('Points vs Time')
plt.xlabel('Points')
plt.ylabel('Time')
plt.show()

