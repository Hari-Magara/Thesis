import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
z = pd.read_csv('steel-thermal.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_xlim([0,180])
plt.plot(z['Temperature'],z['Conductivity'], color='C0')
plt.xlabel('Temperature(°C)', fontsize=14)
plt.ylabel('Conductivity(W/(m°C))', fontsize=14)
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('Steel-conductivity.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_xlim([0,180])
plt.plot(z['Temperature'],z['Specific heat'], color='C0')
plt.xlabel('Temperature(°C)', fontsize=14)
plt.ylabel('Specific Heat(J/(kg°C))', fontsize=14)
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('Steel-specific-heat.pdf', bbox_inches='tight')
plt.show()


     
