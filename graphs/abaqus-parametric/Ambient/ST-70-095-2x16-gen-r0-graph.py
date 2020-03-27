import matplotlib.pyplot as plt
import pandas as pd
#from scipy.interpolate import interp1d
#import numpy as np

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

t1 = pd.read_csv('ST-70-095-2x16-gen-r0.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
#ax.set_ylim(0,65)
#ax.set_xlim(0,180)
plt.plot(t1['Displacement in mm'],t1['Load in kN'], label='ST-70-0.95', color='C0',  markevery=10, ms=4, marker='o')
#plt.plot(xnew,p)
#plt.plot(ynew,q)
plt.xlabel('Displacement(mm)')
plt.ylabel('Load(kN)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('ST-70-095-2x16-gen-r0.pdf', bbox_inches='tight')
plt.show()