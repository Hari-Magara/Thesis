import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('t7-experiment.csv')

#df = pd.read_csv('r7_devc.csv',header=1)
#df.insert(1, 'Time in Minutes',df['Time']/60)
#df.to_csv('r7_devc.csv', sep=',')

r7 = pd.read_csv('t7-r6_devc.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], label='Standard fire curve', color='maroon', markevery=10, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Average-Pb1'], label='Exp-T7-Pb1', color='red', markevery=10, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Average-Pb1-Pb2'], label='Exp-T7-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Average-Pb2'], label='Exp-T7-Pb2', color='C1', markevery=10, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Average-Pb3'], label='Exp-T7-Pb3', color='C2', markevery=10, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Pb4'], label='Exp-T7-Pb3-Pb4', color='C3', markevery=10, ms=4, marker='p')
plt.plot(z['Time in Minutes'],z['Average-Pb4'], label='Exp-T7-Pb4', color='C4', markevery=10, ms=4, marker='h')
plt.plot(r7['Time in Minutes'],r7['Pb1'], label='Fds-T7-Pb1', color='red', linestyle='--', markevery=50, ms=4, marker='*')
plt.plot(r7['Time in Minutes'],r7['Pb1-Pb2'], label='Fds-T7-Pb1-Pb2', color='C0', linestyle='--', markevery=50, ms=4, marker='P')
plt.plot(r7['Time in Minutes'],r7['Pb2'], label='Fds-T7-Pb2', color='C1', linestyle='--', markevery=50, ms=4, marker='X')
plt.plot(r7['Time in Minutes'],r7['Pb3'], label='Fds-T7-Pb3', color='C2', linestyle='--', markevery=50, ms=4, marker='D')
plt.plot(r7['Time in Minutes'],r7['Pb3-Pb4'], label='Fds-T7-Pb3-Pb4', color='C3', linestyle='--', markevery=50, ms=4, marker='<')
plt.plot(r7['Time in Minutes'],r7['Pb4'], label='Fds-T7-Pb4', color='C4', linestyle='--', markevery=50, ms=4, marker='>')
# plt.title('Test8-Exp vs Fds Pb-r7')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T7-r7-Pb-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-HF'], label='Exp-T7-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-CF'], label='Exp-T7-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-HF'], label='Exp-T7-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-CF'], label='Exp-T7-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
plt.plot(r7['Time in Minutes'],r7['FHF'], label='Fds-T7-Fire-HF', color='red', linestyle='--', markevery=50, ms=4, marker='x')
plt.plot(r7['Time in Minutes'],r7['FCF'], label='Fds-T7-Fire-CF', color='C0', linestyle='--', markevery=50, ms=4, marker='p')
plt.plot(r7['Time in Minutes'],r7['AHF'], label='Fds-T7-Amb-HF', color='C1', linestyle='--', markevery=50, ms=4, marker='h')
plt.plot(r7['Time in Minutes'],r7['ACF'], label='Fds-T7-Amb-CF', color='C2', linestyle='--', markevery=50, ms=4, marker='*')
# plt.title('Test8-Exp vs Fds Stud3-r7')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T7-r7-Studs-3-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T7-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T7-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T7-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T7-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
plt.plot(r7['Time in Minutes'],r7['FHF'], label='Fds-T7-Fire-HF', color='red', linestyle='--', markevery=50, ms=4, marker='x')
plt.plot(r7['Time in Minutes'],r7['FCF'], label='Fds-T7-Fire-CF', color='C0', linestyle='--', markevery=50, ms=4, marker='p')
plt.plot(r7['Time in Minutes'],r7['AHF'], label='Fds-T7-Amb-HF', color='C1', linestyle='--', markevery=50, ms=4, marker='h')
plt.plot(r7['Time in Minutes'],r7['ACF-Extra2'], label='Fds-T7-Amb-CF', color='C2', linestyle='--', markevery=50, ms=4, marker='*')
# plt.title('Test8-Exp vs Fds Stud4-r7')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T7-r7-Studs-4-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()