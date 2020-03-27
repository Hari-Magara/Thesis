import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('DS-70-095-2x16-BI-r0_devc.csv')

# df = pd.read_csv('DS-70-095-2x16-BI-r0_devc.csv',header=1)
# df.insert(1, 'Time in Minutes',df['Time']/60)
# df.to_csv('DS-70-095-2x16-BI-r0_devc.csv', sep=',')

r1 = pd.read_csv('DS-70-095-2x16-BI-r0_devc.csv')
r1P = pd.read_csv('DS-70-095-2x16-BI-r1_devc-O.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,250])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(r1['Time in Minutes'],r1['Pb1'], label='Fds-Pb1', color='red', markevery=30, ms=4, marker='o')
plt.plot(r1['Time in Minutes'],r1['Pb1-Pb2'], label='Fds-Pb1-Pb2', color='C0', markevery=30, ms=4, marker='v')
plt.plot(r1['Time in Minutes'],r1['Pb2'], label='Fds-Pb2', color='C1', markevery=30, ms=4, marker='s')
plt.plot(r1['Time in Minutes'],r1['Pb3'], label='Fds-Pb3', color='C2', markevery=30, ms=4, marker='d')
plt.plot(r1['Time in Minutes'],r1['Pb3-Pb4'], label='Fds-Pb3-Pb4', color='C3', markevery=30, ms=4, marker='x')
plt.plot(r1['Time in Minutes'],r1['Pb4'], label='Fds-Pb4', color='C4', markevery=30, ms=4, marker='p')
plt.plot(r1P['Time in Minutes'],r1P['Pb1'], label='Fds-O-Pb1', color='red', markevery=30, ms=4, marker='o', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['Pb1-Pb2'], label='Fds-O-Pb1-Pb2', color='C0', markevery=30, ms=4, marker='v', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['Pb2'], label='Fds-O-Pb2', color='C1', markevery=30, ms=4, marker='s', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['Pb3'], label='Fds-O-Pb3', color='C2', markevery=30, ms=4, marker='d', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['Pb3-Pb4'], label='Fds-O-Pb3-Pb4', color='C3', markevery=30, ms=4, marker='x', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['Pb4'], label='Fds-O-Pb4', color='C4', markevery=30, ms=4, marker='p', linestyle='--')
#plt.title('Test8-Exp vs Fds Pb-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('DS-70-095-2x16-BI-r1-PB.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,250])
plt.plot(r1['Time in Minutes'],r1['FHF-Extra2'], label='Fds-Fire-HF', color='red', markevery=30, ms=4, marker='o')
plt.plot(r1['Time in Minutes'],r1['AHF'], label='Fds-Fire-CF', color='C0', markevery=30, ms=4, marker='v')
plt.plot(r1['Time in Minutes'],r1['ACF'], label='Fds-Amb-HF', color='C1', markevery=30, ms=4, marker='s')
plt.plot(r1['Time in Minutes'],r1['AHF-Extra'], label='Fds-Amb-CF', color='C2', markevery=30, ms=4, marker='d')
plt.plot(r1P['Time in Minutes'],r1P['FHF-Extra2'], label='Fds-O-Fire-HF', color='red', markevery=30, ms=4, marker='o', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['AHF'], label='Fds-O-Fire-CF', color='C0', markevery=30, ms=4, marker='v', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['ACF'], label='Fds-O-Amb-HF', color='C1', markevery=30, ms=4, marker='s', linestyle='--')
plt.plot(r1P['Time in Minutes'],r1P['AHF-Extra'], label='Fds-O-Amb-CF', color='C2', markevery=30, ms=4, marker='d', linestyle='--')
#plt.title('Test8-Exp vs Fds Stud3-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('DS-70-095-2x16-BI-r1-Studs.pdf', bbox_inches='tight')
plt.show()

#ax = plt.axes()     
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#ax.set_xlim([0,250])
#plt.plot(r1['Time in Minutes'],r1['FHF'], label='Fds-Fire-HF', color='red', markevery=30, ms=4, marker='o')
#plt.plot(r1['Time in Minutes'],r1['FCF'], label='Fds-Fire-CF', color='C0', markevery=30, ms=4, marker='v')
#plt.plot(r1['Time in Minutes'],r1['AHF'], label='Fds-Amb-HF', color='C1', markevery=30, ms=4, marker='s')
#plt.plot(r1['Time in Minutes'],r1['ACF'], label='Fds-Amb-CF', color='C2', markevery=30, ms=4, marker='d')
##plt.title('Test8-Exp vs Fds Stud3-r1')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('DS-70-095-2x16-BI-r0-Studs.pdf', bbox_inches='tight')
#plt.show()
