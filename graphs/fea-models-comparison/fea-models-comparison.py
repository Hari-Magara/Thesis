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
sf = pd.read_csv('t1-r4-safir.csv')
a = pd.read_csv('t1-abaqus-r9.csv')
f = pd.read_csv('t1-r61_devc.csv')



ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(z['Time in Minutes'],z['Average-Pb1'], label='Exp-T1-Pb1', color='red', linestyle='-', markevery=30, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Average-Pb1-Pb2'], label='Exp-T1-Pb1-Pb2', color='C0', linestyle='-', markevery=30, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Average-Pb2'], label='Exp-T1-Pb2', color='C1', linestyle='-', markevery=30, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Average-Pb3'], label='Exp-T1-Pb3', color='C2', linestyle='-', markevery=30, ms=4, marker='d')
plt.plot(z['Time in Minutes'],z['Average-Pb3-Pb4'], label='Exp-T1-Pb3-Pb4', color='C3', linestyle='-', markevery=30, ms=4, marker='x')
plt.plot(z['Time in Minutes'],z['Average-Pb4'], label='Exp-T1-Pb4', color='C4', linestyle='-', markevery=30, ms=4, marker='p')
plt.plot(sf['Time in Minutes'],sf['Pb1'], label='SAFIR-T1-Pb1', color='red', markevery=30, ms=4, marker='h', linestyle='--')
plt.plot(sf['Time in Minutes'],sf['Pb1-Pb2'], label='SAFIR-T1-Pb1-Pb2', color='C0', markevery=30, ms=4, marker='+', linestyle='--')
plt.plot(sf['Time in Minutes'],sf['Pb2'], label='SAFIR-T1-Pb2', color='C1', markevery=30, ms=4, marker='*', linestyle='--')
plt.plot(sf['Time in Minutes'],sf['Pb3'], label='SAFIR-T1-Pb3', color='C2', markevery=30, ms=4, marker='X', linestyle='--')
plt.plot(sf['Time in Minutes'],sf['Pb3-Pb4'], label='SAFIR-T1-Pb3-Pb4', color='C3', markevery=30, ms=4, marker='P', linestyle='--')
plt.plot(sf['Time in Minutes'],sf['Pb4'], label='SAFIR-T1-Pb4', color='C4', markevery=30, ms=4, marker='H', linestyle='--')
plt.plot(a['Time in Minutes'],a['Pb1'], label='Abaqus-T1-Pb1', color='red', linestyle=':', markevery=100, ms=4, marker='$T$')
plt.plot(a['Time in Minutes'],a['Pb1-Pb2'], label='Abaqus-T1-Pb1-Pb2', color='C0', linestyle=':', markevery=100, ms=4, marker='2')
plt.plot(a['Time in Minutes'],a['Pb2'], label='Abaqus-T1-Pb2', color='C1', linestyle=':', markevery=100, ms=4, marker='$?$')
plt.plot(a['Time in Minutes'],a['Pb3'], label='Abaqus-T1-Pb3', color='C2', linestyle=':', markevery=100, ms=4, marker='$1$')
plt.plot(a['Time in Minutes'],a['Pb3-Pb4'], label='Abaqus-T1-Pb3-Pb4', color='C3', linestyle=':', markevery=100, ms=4, marker='$2$')
plt.plot(a['Time in Minutes'],a['Pb4'], label='Abaqus-T1-Pb4', color='C4', linestyle=':', markevery=100, ms=4, marker='3')
plt.plot(f['Time in Minutes'],f['Pb1'], label='Fds-T1-Pb1', color='red', linestyle='-.', markevery=100, ms=4, marker='<')
plt.plot(f['Time in Minutes'],f['Pb1-Pb2'], label='Fds-T1-Pb1-Pb2', color='C0', linestyle='-.', markevery=100, ms=4, marker='>')
plt.plot(f['Time in Minutes'],f['Pb2'], label='Fds-T1-Pb2', color='C1', linestyle='-.', markevery=100, ms=4, marker='1')
plt.plot(f['Time in Minutes'],f['Pb3'], label='Fds-T1-Pb3', color='C2', linestyle='-.', markevery=100, ms=4, marker='D')
plt.plot(f['Time in Minutes'],f['Pb3-Pb4'], label='Fds-T1-Pb3-Pb4', color='C3', linestyle='-.', markevery=100, ms=4, marker='$!$')
plt.plot(f['Time in Minutes'],f['Pb4'], label='Fds-T1-Pb4', color='C4', linestyle='-.', markevery=100, ms=4, marker='$@$')

#plt.title('Test1-Exp vs SAFIR PB-R4')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T1-Plasterboard-fe-comparison.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T1-Stud4-Mid-Fire-HF', color='red', markevery=30, ms=4, marker='o')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T1-Stud4-Mid-Fire-CF', color='C0', markevery=30, ms=4, marker='v')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T1-Stud4-Mid-Amb-HF', color='C1', markevery=30, ms=4, marker='s')
plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T1-Stud4-Mid-Amb-CF', color='C2', markevery=30, ms=4, marker='d')
plt.plot(sf['Time in Minutes'],sf['Fire-HF'], label='SAFIR-T1-Fire-HF', color='red', linestyle='--', markevery=30, ms=4, marker='x')
plt.plot(sf['Time in Minutes'],sf['Fire-CF'], label='SAFIR-T1-Fire-CF', color='C0', linestyle='--', markevery=30, ms=4, marker='p')
plt.plot(sf['Time in Minutes'],sf['Amb-HF'], label='SAFIR-T1-Amb-HF', color='C1', linestyle='--', markevery=30, ms=4, marker='h')
plt.plot(sf['Time in Minutes'],sf['Amb-CF'], label='SAFIR-T1-Amb-CF', color='C2', linestyle='--', markevery=30, ms=4, marker='+')
plt.plot(a['Time in Minutes'],a['Fire-HF'], label='Abaqus-T1-Fire-HF', color='red', linestyle=':', markevery=100, ms=4, marker='1')
plt.plot(a['Time in Minutes'],a['Fire-CF'], label='Abaqus-T1-Fire-CF', color='C0', linestyle=':', markevery=100, ms=4, marker='<')
plt.plot(a['Time in Minutes'],a['Amb-HF'], label='Abaqus-T1-Amb-HF', color='C1', linestyle=':', markevery=100, ms=4, marker='>')
plt.plot(a['Time in Minutes'],a['Amb-CF'], label='Abaqus-T1-Amb-CF', color='C2', linestyle=':', markevery=100, ms=4, marker='3')
plt.plot(f['Time in Minutes'],f['FHF'], label='Fds-T1-Fire-HF', color='red', linestyle='-.', markevery=100, ms=4, marker='X')
plt.plot(f['Time in Minutes'],f['FCF'], label='Fds-T1-Fire-CF', color='C0', linestyle='-.', markevery=100, ms=4, marker='H')
plt.plot(f['Time in Minutes'],f['AHF'], label='Fds-T1-Amb-HF', color='C1', linestyle='-.', markevery=100, ms=4, marker='D')
plt.plot(f['Time in Minutes'],f['ACF'], label='Fds-T1-Amb-CF', color='C2', linestyle='-.', markevery=100, ms=4, marker='*')

#plt.title('Test1-Exp vs SAFIR Stud3-R4')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-Studs-4-fe-comparison.pdf', bbox_inches='tight')
plt.show()

# ax = plt.axes()     
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.xaxis.label.set_size(12)
# ax.yaxis.label.set_size(12)
# ax.set_xlim([0,240])
# plt.plot(f['Time in Minutes'],f['Fire-HF'], label='SAFIR-T1-Fire-HF', color='red', linestyle='--', markevery=30, ms=4, marker='o')
# plt.plot(f['Time in Minutes'],f['Fire-CF'], label='SAFIR-T1-Fire-CF', color='C0', linestyle='--', markevery=30, ms=4, marker='v')
# plt.plot(f['Time in Minutes'],f['Amb-HF'], label='SAFIR-T1-Amb-HF', color='C1', linestyle='--', markevery=30, ms=4, marker='s')
# plt.plot(f['Time in Minutes'],f['Amb-CF'], label='SAFIR-T1-Amb-CF', color='C2', linestyle='--', markevery=30, ms=4, marker='d')
# plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-HF'], label='Exp-T1-Stud4-Mid-Fire-HF', color='red', markevery=30, ms=4, marker='x')
# plt.plot(z['Time in Minutes'],z['Stud4-Mid-Fire-CF'], label='Exp-T1-Stud4-Mid-Fire-CF', color='C0', markevery=30, ms=4, marker='p')
# plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-HF'], label='Exp-T1-Stud4-Mid-Amb-HF', color='C1', markevery=30, ms=4, marker='h')
# plt.plot(z['Time in Minutes'],z['Stud4-Mid-Amb-CF'], label='Exp-T1-Stud4-Mid-Amb-CF', color='C2', markevery=30, ms=4, marker='*')
# #plt.title('Test1-Exp vs SAFIR Stud4-R4')
# plt.xlabel('Time(min)')
# plt.ylabel('Temperature(°C)')
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('T1-r4-Studs-4-Safir-vs-Exp.pdf', bbox_inches='tight')
# plt.show()

