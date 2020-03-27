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
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(z['Time in Minutes'],z['Average-Pb1'], label='Exp-T1-Pb1', color='red', linestyle='--')
plt.plot(z['Time in Minutes'],z['Average-Pb1-Pb2'], label='Exp-T1-Pb1-Pb2', color='C0', linestyle='--')
plt.plot(z['Time in Minutes'],z['Average-Pb2'], label='Exp-T1-Pb2', color='C1', linestyle='--')
plt.plot(z['Time in Minutes'],z['Average-Pb3'], label='Exp-T1-Pb3', color='C2', linestyle='--')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Pb4'], label='Exp-T1-Pb3-Pb4', color='C3', linestyle='--')
plt.plot(z['Time in Minutes'],z['Average-Pb4'], label='Exp-T1-Pb4', color='C4', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Pb1'], label='SAFIR-T1-Pb1', color='red')
plt.plot(r4['Time in Minutes'],r4['Pb1-Pb2'], label='SAFIR-T1-Pb1-Pb2', color='C0')
plt.plot(r4['Time in Minutes'],r4['Pb2'], label='SAFIR-T1-Pb2', color='C1')
plt.plot(r4['Time in Minutes'],r4['Pb3'], label='SAFIR-T1-Pb3', color='C2')
plt.plot(r4['Time in Minutes'],r4['Pb3-Pb4'], label='SAFIR-T1-Pb3-Pb4', color='C3')
plt.plot(r4['Time in Minutes'],r4['Pb4'], label='SAFIR-T1-Pb4', color='C4')
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
plt.plot(r4['Time in Minutes'],r4['Fire-HF'], label='SAFIR-T1-Fire-HF', color='red', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Fire-CF'], label='SAFIR-T1-Fire-CF', color='C0', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Amb-HF'], label='SAFIR-T1-Amb-HF', color='C1', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Amb-CF'], label='SAFIR-T1-Amb-CF', color='C2', linestyle='--')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-HF'], label='Exp-T1-Fire-HF', color='red')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Fire-CF'], label='Exp-T1-Fire-CF', color='C0')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-HF'], label='Exp-T1-Amb-HF', color='C1')
plt.plot(z['Time in Minutes'],z['Stud3-Mid-Amb-CF'], label='Exp-T1-Amb-CF', color='C2')
#plt.title('Test1-Exp vs SAFIR Stud3-R4')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-r4-Studs-3.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(r4['Time in Minutes'],r4['Fire-HF'], label='SAFIR-T1-Fire-HF', color='red', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Fire-CF'], label='SAFIR-T1-Fire-CF', color='C0', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Amb-HF'], label='SAFIR-T1-Amb-HF', color='C1', linestyle='--')
plt.plot(r4['Time in Minutes'],r4['Amb-CF'], label='SAFIR-T1-Amb-CF', color='C2', linestyle='--')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T1-Fire-HF', color='red')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T1-Fire-CF', color='C0')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T1-Amb-HF', color='C1')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T1-Amb-CF', color='C2')
#plt.title('Test1-Exp vs SAFIR Stud4-R4')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-r4-Studs-4.pdf', bbox_inches='tight')
plt.show()

