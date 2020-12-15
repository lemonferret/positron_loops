import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy as copy






name = "k15_a3.106_ecut"
data=pd.read_csv(name, delim_whitespace=True, skipinitialspace=True,  engine="python", skiprows = 0, skipfooter =1, header = None)

Ecut  = np.arange(200, 550, 10)
F = copy.deepcopy(data[3][1:])
E = copy.deepcopy(data[5][1:])
dE = copy.deepcopy(data[8][1:])
Ecorr = copy.deepcopy(data[9][1:])
N = 2


Ecut = np.array(Ecut)
F = np.array(F)
E = np.array(E)
dE = np.array(dE)
Ecorr = np.array(Ecorr)

de = []
for i in dE: 
	i = i[1:]
	de.extend([i])
dE = np.array(de)



Ecut = Ecut.astype(np.float)
F = F.astype(np.float)
E = E.astype(np.float)
dE = dE.astype(np.float)
Ecorr = Ecorr.astype(np.float)



fig = plt.figure() 
ax1 = fig.add_subplot(111)

ax1.plot(Ecut, F, marker='x', color='blue', linestyle='dotted', label='(k15) F')
ax1.plot(Ecut, F+N*Ecorr, marker='x', color='lightblue', linestyle='dotted', label='(k15) F+N*Ecorr')


ax1.legend()

ax1.plot([400, 400], [-8.15, -25.4], color='black', linestyle='dashed')


ax1.set_ylabel('F')
ax1.set_ylabel('F')
ax1.set_xlabel('Ecut')
ax1.set_title('Ecut, a=3.106, dE<0.01')

plt.show()
