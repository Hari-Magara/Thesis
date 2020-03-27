import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('t4-noopen.csv')
z1 = pd.read_csv('t4-open.csv')

#df = pd.read_csv('z_devc.csv',header=1)
#df.insert(1, 'Time in Minutes',df['Time']/60)
#df.to_csv('z_devc.csv', sep=',')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], label='Standard fire curve', color='maroon')
plt.plot(z['Time in Minutes'],z['Pb1'], label='Fds-T4-Pb1', color='red', markevery=100, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Pb1-Pb2'], label='Fds-T4-Pb1-Pb2', color='C0', markevery=100, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Pb2'], label='Fds-T4-Pb2', color='C1', markevery=100, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Pb3'], label='Fds-T4-Pb3', color='C2', markevery=100, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Pb3-Pb4'], label='Fds-T4-Pb3-Pb4', color='C3', markevery=100, ms=4, marker='h')
plt.plot(z['Time in Minutes'],z['Pb4'], label='Fds-T4-Pb4', color='C4', markevery=100, ms=4, marker='p')
plt.plot(z1['Time in Minutes'],z1['Pb1'], label='Fds-T4-Pb1-O', color='red', linestyle='--', markevery=100, ms=4, marker='x')
plt.plot(z1['Time in Minutes'],z1['Pb1-Pb2'], label='Fds-T4-Pb1-Pb2-O', color='C0', linestyle='--', markevery=100, ms=4, marker='+')
plt.plot(z1['Time in Minutes'],z1['Pb2'], label='Fds-T4-Pb2-O', color='C1', linestyle='--', markevery=100, ms=4, marker='*')
plt.plot(z1['Time in Minutes'],z1['Pb3'], label='Fds-T4-Pb3-O', color='C2', linestyle='--', markevery=100, ms=4, marker='<')
plt.plot(z1['Time in Minutes'],z1['Pb3-Pb4'], label='Fds-T4-Pb3-Pb4-O', color='C3', linestyle='--', markevery=100, ms=4, marker='>')
plt.plot(z1['Time in Minutes'],z1['Pb4'], label='Fds-T4-Pb4-O', color='C4', linestyle='--', markevery=100, ms=4, marker='1')
#plt.title('Test1-Exp vs Fds Pb-z')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T4-Pb-Fds-openup.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['FHF'], label='Fds-T4-Fire-HF', color='red', markevery=100, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['ACF-Extra2'], label='Fds-T4-Fire-CF', color='C0', markevery=100, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['AHF'], label='Fds-T4-Amb-HF', color='C1', markevery=100, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['AHF-Extra'], label='Fds-T4-Amb-CF', color='C2', markevery=100, ms=4, marker='d')
plt.plot(z1['Time in Minutes'],z1['FHF'], label='Fds-T4-Fire-HF-O', color='red', linestyle='--', markevery=100, ms=4, marker='x')
plt.plot(z1['Time in Minutes'],z1['ACF-Extra2'], label='Fds-T4-Fire-CF-O', color='C0', linestyle='--', markevery=100, ms=4, marker='p')
plt.plot(z1['Time in Minutes'],z1['AHF'], label='Fds-T4-Amb-HF-O', color='C1', linestyle='--', markevery=100, ms=4, marker='h')
plt.plot(z1['Time in Minutes'],z1['AHF-Extra'], label='Fds-T4-Amb-CF-O', color='C2', linestyle='--', markevery=100, ms=4, marker='*')
#plt.title('Test1-Exp vs Fds Stud3-z')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T4-Studs-Fds-openup.pdf', bbox_inches='tight')
plt.show()
