import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy as copy
name =  ["e400_a3.106_k"]#[name03, name04]

#colors = [ 'palevioletred', 'lightsteelblue', 'lightgreen', 'thistle']#, 'wheat', 'powderblue', 'thistle'] #plum khaki
colors = ['green']#, 'thistle']#, 'wheat', 'powderblue', 'thistle'] #plum khaki
labels = ["Ecut = 400, sigma= 0.2"]

fig = plt.figure() 
ax1 = fig.add_subplot(111)

for i in range(0, len(name)):
	data=pd.read_csv(name[i], delim_whitespace=True, skipinitialspace=True,  engine="python", skiprows = 0, skipfooter =0, header = None)

	k = copy.deepcopy(data[0])

	F = copy.deepcopy(data[3])
	E = copy.deepcopy(data[5])
	dE = copy.deepcopy(data[8])
	F = np.array(F)
	E = np.array(E)
	dE = np.array(dE)

	de = []
	for a in dE: 
		a = a[1:]
		de.extend([a])
	dE = np.array(de)

	F = F.astype(np.float)
	E = E.astype(np.float)
	dE = dE.astype(np.float)


	ax1.plot(k, F, marker= '.', color=colors[i], linestyle='dashed', label=labels[i])
	


ax1.legend()
#ax1.text(0.18, 0.95, 'F(k17, s0.2) - F(k27, s0.1) = -0.00058eV', transform=ax1.transAxes, fontsize=10, verticalalignment='top')
#ax1.plot([27, 27], [-27, -26], color='black', linestyle='dashed')
ax1.plot([15, 15], [-20, -25], color='black', linestyle='dashed')

ax1.set_ylabel('Total Energy')
ax1.set_xlabel('k-grid')
ax1.set_title('Kgrid, Ecut=400, a=3.106, dE<0.01eV')
#ax1.set_ylim([-26.038, -26.043])
#ax1.set_xlim([15, 28])


plt.show()
