import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
z = pd.read_csv('Test9-Specimen_RawData_4.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,0.04])
ax.set_ylim([0,700])
plt.plot(z['Tensile strain'],z['Tensile stress'], color='C0', markevery=200, ms=4, marker='o')
plt.plot(z['Offset strain'],z['Tensile stress offset'], color='red', markevery=200, ms=4, marker='v')
#plt.title('AT1 - Load vs Axial Displacement')
plt.xlabel('Strain', fontsize=14)
plt.ylabel('Stress (MPa)', fontsize=14)
#plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('Test9-Specimen_RawData_4.pdf', bbox_inches='tight')
plt.show()


 