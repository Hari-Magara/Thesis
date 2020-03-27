import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('t8-experiment.csv')

# df = pd.read_csv('t8-r23_devc.csv',header=1)
# df.insert(1, 'Time in Minutes',df['Time']/60)
# df.to_csv('t8-r23_devc.csv', sep=',')

r23 = pd.read_csv('t8-r23_devc.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], label='Standard fire curve', color='maroon', markevery=20, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Average-Pb1'], label='Exp-T8-Pb1', color='red', markevery=20, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Average-Pb1-Pb2'], label='Exp-T8-Pb1-Pb2', color='C0', markevery=20, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Average-Pb2'], label='Exp-T8-Pb2', color='C1', markevery=20, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Fire'], label='Exp-T8-Pb3-Fire', color='C2', markevery=20, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Amb'], label='Exp-T8-Pb3-Amb', color='C3', markevery=20, ms=4, marker='p')
plt.plot(z['Time in Minutes'],z['Average-Pb4'], label='Exp-T8-Pb4', color='C4', markevery=20, ms=4, marker='h')
plt.plot(z['Time in Minutes'],z['Average-Pb4-Pb5'], label='Exp-T8-Pb4-Pb5', color='C5', markevery=20, ms=4, marker='*')
plt.plot(z['Time in Minutes'],z['Average-Pb5'], label='Exp-T8-Pb5', color='C6', markevery=20, ms=4, marker='+')
plt.plot(r23['Time in Minutes'],r23['Pb2'], label='Fds-T8-Pb1', color='red', linestyle='--', markevery=50, ms=4, marker='<')
plt.plot(r23['Time in Minutes'],r23['Pb1-Pb2'], label='Fds-T8-Pb1-Pb2', color='C0', linestyle='--', markevery=50, ms=4, marker='>')
plt.plot(r23['Time in Minutes'],r23['Pb1'], label='Fds-T8-Pb2', color='C1', linestyle='--', markevery=50, ms=4, marker='^')
plt.plot(r23['Time in Minutes'],r23['Pb3-Amb'], label='Fds-T8-Pb3-Fire', color='C2', linestyle='--', markevery=50, ms=4, marker='H')
plt.plot(r23['Time in Minutes'],r23['Pb3-Fire'], label='Fds-T8-Pb3-Amb', color='C3', linestyle='--', markevery=50, ms=4, marker='P')
plt.plot(r23['Time in Minutes'],r23['Pb4'], label='Fds-T8-Pb4', color='C4', linestyle='--', markevery=50, ms=4, marker='D')
plt.plot(r23['Time in Minutes'],r23['Pb4-Pb5'], label='Fds-T8-Pb4-Pb5', color='C5', linestyle='--', markevery=50, ms=4, marker='|')
plt.plot(r23['Time in Minutes'],r23['Pb5'], label='Fds-T8-Pb5', color='C6', linestyle='--', markevery=50, ms=4, marker='8')
#plt.title('Test3-Exp vs Fds Pb-r23')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T8-r23-Pb-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-HF'], label='Exp-T8-Fire-HF', color='red', markevery=20, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-CF'], label='Exp-T8-Fire-CF', color='C0', markevery=20, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-HF'], label='Exp-T8-Amb-HF', color='C1', markevery=20, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-CF'], label='Exp-T8-Amb-CF', color='C2', markevery=20, ms=4, marker='d')
plt.plot(r23['Time in Minutes'],r23['FHF'], label='Fds-T8-Fire-HF', color='red', linestyle='--', markevery=50, ms=4, marker='x')
plt.plot(r23['Time in Minutes'],r23['FCF'], label='Fds-T8-Fire-CF', color='C0', linestyle='--', markevery=50, ms=4, marker='p')
plt.plot(r23['Time in Minutes'],r23['AHF'], label='Fds-T8-Amb-HF', color='C1', linestyle='--', markevery=50, ms=4, marker='h')
plt.plot(r23['Time in Minutes'],r23['ACF'], label='Fds-T8-Amb-CF', color='C2', linestyle='--', markevery=50, ms=4, marker='*')
#plt.title('Test3-Exp vs Fds Stud3-r23')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-r23-Studs-3-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T8-Fire-HF', color='red', markevery=20, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T8-Fire-CF', color='C0', markevery=20, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T8-Amb-HF', color='C1', markevery=20, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T8-Amb-CF', color='C2', markevery=20, ms=4, marker='d')
plt.plot(r23['Time in Minutes'],r23['FHF'], label='Fds-T8-Fire-HF', color='red', linestyle='--', markevery=50, ms=4, marker='x')
plt.plot(r23['Time in Minutes'],r23['FCF'], label='Fds-T8-Fire-CF', color='C0', linestyle='--', markevery=50, ms=4, marker='p')
plt.plot(r23['Time in Minutes'],r23['AHF'], label='Fds-T8-Amb-HF', color='C1', linestyle='--', markevery=50, ms=4, marker='h')
plt.plot(r23['Time in Minutes'],r23['ACF-Extra2'], label='Fds-T8-Amb-CF', color='C2', linestyle='--', markevery=50, ms=4, marker='*')
#plt.title('Test3-Exp vs Fds Stud4-r23')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-r23-Studs-4-Fds-vs-Exp.pdf', bbox_inches='tight')
plt.show()