import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('t9-experiment.csv')

#df = pd.read_csv('r1_devc.csv',header=1)
#df.insert(1, 'Time in Minutes',df['Time']/60)
#df.to_csv('r1_devc.csv', sep=',')

r1 = pd.read_csv('t9-r1_devc.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], label='Standard fire curve', color='maroon', markevery=20, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Average-Pb1'], label='Exp-T9-Pb1', color='red', markevery=20, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Average-Pb1-Pb2'], label='Exp-T9-Pb1-Pb2', color='C0', markevery=20, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Average-Pb2'], label='Exp-T9-Pb2', color='C1', markevery=20, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Average-Pb3'], label='Exp-T9-Pb3', color='C2', markevery=20, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Pb4'], label='Exp-T9-Pb3-Pb4', color='C3', markevery=20, ms=4, marker='p')
plt.plot(z['Time in Minutes'],z['Average-Pb4'], label='Exp-T9-Pb4', color='C4', markevery=20, ms=4, marker='h')
plt.plot(r1['Time in Minutes'],r1['Pb1'], label='Fds-T9-Pb1', color='red', linestyle='--', markevery=50, ms=4, marker='*')
plt.plot(r1['Time in Minutes'],r1['Pb1-Pb2'], label='Fds-T9-Pb1-Pb2', color='C0', linestyle='--', markevery=50, ms=4, marker='+')
plt.plot(r1['Time in Minutes'],r1['Pb2'], label='Fds-T9-Pb2', color='C1', linestyle='--', markevery=50, ms=4, marker='P')
plt.plot(r1['Time in Minutes'],r1['Pb3'], label='Fds-T9-Pb3', color='C2', linestyle='--', markevery=50, ms=4, marker='H')
plt.plot(r1['Time in Minutes'],r1['Pb3-Pb4'], label='Fds-T9-Pb3-Pb4', color='C3', linestyle='--', markevery=50, ms=4, marker='<')
plt.plot(r1['Time in Minutes'],r1['Pb4'], label='Fds-T9-Pb4', color='C4', linestyle='--', markevery=50, ms=4, marker='D')
# plt.title('Test6-Exp vs Fds Pb-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T9-r1-Pb-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-HF'], label='Exp-T9-Fire-HF', color='red', markevery=20, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-CF'], label='Exp-T9-Fire-CF', color='C0', markevery=20, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-HF'], label='Exp-T9-Amb-HF', color='C1', markevery=20, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-CF'], label='Exp-T9-Amb-CF', color='C2', markevery=20, ms=4, marker='d')
plt.plot(r1['Time in Minutes'],r1['FHF'], label='Fds-T9-Fire-HF', color='red', linestyle='--', markevery=50, ms=4, marker='x')
plt.plot(r1['Time in Minutes'],r1['FCF'], label='Fds-T9-Fire-CF', color='C0', linestyle='--', markevery=50, ms=4, marker='p')
plt.plot(r1['Time in Minutes'],r1['AHF'], label='Fds-T9-Amb-HF', color='C1', linestyle='--', markevery=50, ms=4, marker='h')
plt.plot(r1['Time in Minutes'],r1['ACF'], label='Fds-T9-Amb-CF', color='C2', linestyle='--', markevery=50, ms=4, marker='*')
# plt.title('Test6-Exp vs Fds Stud3-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-r1-Studs-3-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T9-Fire-HF', color='red', markevery=20, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T9-Fire-CF', color='C0', markevery=20, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T9-Amb-HF', color='C1', markevery=20, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T9-Amb-CF', color='C2', markevery=20, ms=4, marker='d')
plt.plot(r1['Time in Minutes'],r1['FHF'], label='Fds-T9-Fire-HF', color='red', linestyle='--', markevery=50, ms=4, marker='x')
plt.plot(r1['Time in Minutes'],r1['FCF'], label='Fds-T9-Fire-CF', color='C0', linestyle='--', markevery=50, ms=4, marker='p')
plt.plot(r1['Time in Minutes'],r1['AHF'], label='Fds-T9-Amb-HF', color='C1', linestyle='--', markevery=50, ms=4, marker='h')
plt.plot(r1['Time in Minutes'],r1['ACF-Extra2'], label='Fds-T9-Amb-CF', color='C2', linestyle='--', markevery=50, ms=4, marker='*')
# plt.title('Test6-Exp vs Fds Stud4-r1')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-r1-Studs-4-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()