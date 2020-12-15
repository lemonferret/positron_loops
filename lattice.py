import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy as copy
name = "k15_e400_a"
data=pd.read_csv(name, delim_whitespace=True, skipinitialspace=True,  engine="python", skiprows = 0, skipfooter =1, header = None)


a = copy.deepcopy(data[0][1:])
F = copy.deepcopy(data[3][1:])
N = 2
a = np.array(a)
F = np.array(F)


a = a.astype(np.float)
F = F.astype(np.float)


print(a)
fig = plt.figure() 
ax1 = fig.add_subplot(111)
print(F)

ax1.plot(a, F, marker='.', color='palevioletred', linestyle='solid', label='Ecut=400eV, k-grid=15, sigma=0.2')

ax1.legend()


ax1.legend()

ax1.plot([3.106, 3.106], [-25, -24], color='black', linestyle='dashed')



ax1.set_ylabel('F')
ax1.set_xlabel('a')
ax1.set_title('Lattice param as a func. of energy')

plt.show()
