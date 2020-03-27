import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
z = pd.read_csv('t1-experiment.csv')
r4 = pd.read_csv('t1-r4-safir.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon', markevery=30, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Average-Pb1'], label='Exp-T1-Pb1', color='red', linestyle='--', markevery=30, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Average-Pb1-Pb2'], label='Exp-T1-Pb1-Pb2', color='C0', linestyle='--', markevery=30, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Average-Pb2'], label='Exp-T1-Pb2', color='C1', linestyle='--', markevery=30, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Average-Pb3'], label='Exp-T1-Pb3', color='C2', linestyle='--', markevery=30, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Pb4'], label='Exp-T1-Pb3-Pb4', color='C3', linestyle='--', markevery=30, ms=4, marker='p')
plt.plot(z['Time in Minutes'],z['Average-Pb4'], label='Exp-T1-Pb4', color='C4', linestyle='--', markevery=30, ms=4, marker='h')
plt.plot(r4['Time in Minutes'],r4['Pb1'], label='SAFIR-T1-Pb1', color='red', markevery=30, ms=4, marker='+')
plt.plot(r4['Time in Minutes'],r4['Pb1-Pb2'], label='SAFIR-T1-Pb1-Pb2', color='C0', markevery=30, ms=4, marker='*')
plt.plot(r4['Time in Minutes'],r4['Pb2'], label='SAFIR-T1-Pb2', color='C1', markevery=30, ms=4, marker='<')
plt.plot(r4['Time in Minutes'],r4['Pb3'], label='SAFIR-T1-Pb3', color='C2', markevery=30, ms=4, marker='>')
plt.plot(r4['Time in Minutes'],r4['Pb3-Pb4'], label='SAFIR-T1-Pb3-Pb4', color='C3', markevery=30, ms=4, marker='P')
plt.plot(r4['Time in Minutes'],r4['Pb4'], label='SAFIR-T1-Pb4', color='C4', markevery=30, ms=4, marker='H')
#plt.title('Test1-Exp vs SAFIR PB-R4')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T1-r4-Plasterboard-Safir-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(r4['Time in Minutes'],r4['Fire-HF'], label='SAFIR-T1-Fire-HF', color='red', linestyle='--', markevery=30, ms=4, marker='o')
plt.plot(r4['Time in Minutes'],r4['Fire-CF'], label='SAFIR-T1-Fire-CF', color='C0', linestyle='--', markevery=30, ms=4, marker='v')
plt.plot(r4['Time in Minutes'],r4['Amb-HF'], label='SAFIR-T1-Amb-HF', color='C1', linestyle='--', markevery=30, ms=4, marker='s')
plt.plot(r4['Time in Minutes'],r4['Amb-CF'], label='SAFIR-T1-Amb-CF', color='C2', linestyle='--', markevery=30, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-HF'], label='Exp-T1-Stud3-Mid-Fire-HF', color='red', markevery=30, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-CF'], label='Exp-T1-Stud3-Mid-Fire-CF', color='C0', markevery=30, ms=4, marker='p')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-HF'], label='Exp-T1-Stud3-Mid-Amb-HF', color='C1', markevery=30, ms=4, marker='h')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-CF'], label='Exp-T1-Stud3-Mid-Amb-CF', color='C2', markevery=30, ms=4, marker='*')
#plt.title('Test1-Exp vs SAFIR Stud3-R4')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-r4-Studs-3-Safir-vs-Exp.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(r4['Time in Minutes'],r4['Fire-HF'], label='SAFIR-T1-Fire-HF', color='red', linestyle='--', markevery=30, ms=4, marker='o')
plt.plot(r4['Time in Minutes'],r4['Fire-CF'], label='SAFIR-T1-Fire-CF', color='C0', linestyle='--', markevery=30, ms=4, marker='v')
plt.plot(r4['Time in Minutes'],r4['Amb-HF'], label='SAFIR-T1-Amb-HF', color='C1', linestyle='--', markevery=30, ms=4, marker='s')
plt.plot(r4['Time in Minutes'],r4['Amb-CF'], label='SAFIR-T1-Amb-CF', color='C2', linestyle='--', markevery=30, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T1-Stud4-Mid-Fire-HF', color='red', markevery=30, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T1-Stud4-Mid-Fire-CF', color='C0', markevery=30, ms=4, marker='p')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T1-Stud4-Mid-Amb-HF', color='C1', markevery=30, ms=4, marker='h')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T1-Stud4-Mid-Amb-CF', color='C2', markevery=30, ms=4, marker='*')
#plt.title('Test1-Exp vs SAFIR Stud4-R4')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-r4-Studs-4-Safir-vs-Exp.pdf', bbox_inches='tight')
plt.show()

