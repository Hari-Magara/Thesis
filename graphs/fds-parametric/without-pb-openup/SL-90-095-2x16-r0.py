import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('SL-90-095-2x16-r0_devc.csv')

df = pd.read_csv('SL-90-095-2x16-r0_devc.csv',header=1)
df.insert(1, 'Time in Minutes',df['Time']/60)
df.to_csv('SL-90-095-2x16-r0_devc.csv', sep=',')

r1 = pd.read_csv('SL-90-095-2x16-r0_devc.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,250])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(r1['Time in Minutes'],r1['Pb2'], label='Fds-Pb1', color='red', markevery=30, ms=4, marker='o')
plt.plot(r1['Time in Minutes'],r1['Pb1-Pb2'], label='Fds-Pb1-Pb2', color='C0', markevery=30, ms=4, marker='v')
plt.plot(r1['Time in Minutes'],r1['Pb1'], label='Fds-Pb2', color='C1', markevery=30, ms=4, marker='s')
plt.plot(r1['Time in Minutes'],r1['Pb3-Fire'], label='Fds-Pb3-Fire', color='C7', markevery=30, ms=4, marker='d')
plt.plot(r1['Time in Minutes'],r1['Pb3-Amb'], label='Fds-Pb3-Fire', color='C8', markevery=30, ms=4, marker='x')
plt.plot(r1['Time in Minutes'],r1['Pb4'], label='Fds-Pb4', color='C2', markevery=30, ms=4, marker='p')
plt.plot(r1['Time in Minutes'],r1['Pb4-Pb5'], label='Fds-Pb4-Pb5', color='C4', markevery=30, ms=4, marker='h')
plt.plot(r1['Time in Minutes'],r1['Pb5'], label='Fds-Pb5', color='C6', markevery=30, ms=4, marker='*')
#plt.title('Test8-Exp vs Fds Pb-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('SL-90-095-2x16-r0-PB.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,250])
plt.plot(r1['Time in Minutes'],r1['FHF'], label='Fds-Fire-HF', color='red', markevery=30, ms=4, marker='o')
plt.plot(r1['Time in Minutes'],r1['FCF'], label='Fds-Fire-CF', color='C0', markevery=30, ms=4, marker='v')
plt.plot(r1['Time in Minutes'],r1['AHF'], label='Fds-Amb-HF', color='C1', markevery=30, ms=4, marker='s')
plt.plot(r1['Time in Minutes'],r1['ACF'], label='Fds-Amb-CF', color='C2', markevery=30, ms=4, marker='d')
#plt.title('Test8-Exp vs Fds Stud3-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('SL-90-095-2x16-r0-Studs.pdf', bbox_inches='tight')
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
#plt.savefig('SL-90-095-2x16-r0-Studs.pdf', bbox_inches='tight')
#plt.show()
