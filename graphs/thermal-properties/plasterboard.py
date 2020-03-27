import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
z = pd.read_csv('plasterboard.csv')

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
plt.savefig('Plasterboard-conductivity.pdf', bbox_inches='tight')
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
plt.savefig('Plasterboard-specific-heat.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_xlim([0,180])
plt.plot(z['Temperature'],z['Density'], color='C0')
plt.xlabel('Temperature(°C)', fontsize=14)
r'This is an expression $e^{\sin(\omega\phi)}$'
plt.ylabel(r'Density(kg/m$\mathregular{^3}$)', fontsize=14)
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('Plasterboard-density.pdf', bbox_inches='tight')
plt.show()

     
