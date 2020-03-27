import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
t1 = pd.read_csv('t1.csv')
t4 = pd.read_csv('t4.csv')
sst1 = pd.read_csv('ss-t1.csv')
sst2 = pd.read_csv('ss-t2.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t1['Time in Minutes'],t1['Average-Pb1'], label='T1-Pb1', color='red',  markevery=10, ms=4, marker='o')
plt.plot(t4['Time in Minutes'],t4['Average-Pb1'], linestyle='--', label='T4-Pb1', color='red',  markevery=10, ms=4, marker='v')
plt.plot(sst1['Time in Minutes'],sst1['Average-Pb1'], linestyle=':', label='SS-T1-Pb1', color='red',  markevery=10, ms=4, marker='s')
plt.plot(sst2['Time in Minutes'],sst2['Average-Pb1'], linestyle='-.', label='SS-T2-Pb1', color='red',  markevery=10, ms=4, marker='d')
plt.plot(t1['Time in Minutes'],t1['Average-Pb1-Pb2'], label='T1-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='x')
plt.plot(t4['Time in Minutes'],t4['Average-Pb1-Pb2'], linestyle='--', label='T4-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='p')
plt.plot(sst1['Time in Minutes'],sst1['Average-Pb1-Pb2'], linestyle=':', label='SS-T1-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='x')
plt.plot(sst2['Time in Minutes'],sst2['Average-Pb1-Pb2'], linestyle='-.', label='SS-T2-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='d')
plt.plot(t1['Time in Minutes'],t1['Average-Pb2'], label='T1-Pb2', color='C1',  markevery=10, ms=4, marker='h')
plt.plot(t4['Time in Minutes'],t4['Average-Pb2'], linestyle='--', label='T4-Pb2', color='C1',  markevery=10, ms=4, marker='1')
plt.plot(sst1['Time in Minutes'],sst1['Average-Pb2'], linestyle=':', label='SS-T1-Pb2', color='C1',  markevery=10, ms=4, marker='+')
plt.plot(sst2['Time in Minutes'],sst2['Average-Pb2'], linestyle='-.', label='SS-T2-Pb2', color='C1',  markevery=10, ms=4, marker='*')
plt.plot(t1['Time in Minutes'],t1['Average-Pb3'], label='T1-Pb3', color='C2',  markevery=10, ms=4, marker='P')
plt.plot(t4['Time in Minutes'],t4['Average-Pb3'], linestyle='--', label='T4-Pb3', color='C2',  markevery=10, ms=4, marker='X')
plt.plot(sst1['Time in Minutes'],sst1['Average-Pb3'], linestyle=':', label='SS-T1-Pb3', color='C2',  markevery=10, ms=4, marker='D')
plt.plot(sst2['Time in Minutes'],sst2['Average-Pb3'], linestyle='-.', label='SS-T2-Pb3', color='C2',  markevery=10, ms=4, marker='H')
plt.plot(t1['Time in Minutes'],t1['Average-Pb3-Pb4'], label='T1-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='2')
plt.plot(t4['Time in Minutes'],t4['Average-Pb3-Pb4'], linestyle='--', label='T4-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='3')
plt.plot(sst1['Time in Minutes'],sst1['Average-Pb3-Pb4'], linestyle=':', label='SS-T1-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='4')
plt.plot(sst2['Time in Minutes'],sst2['Average-Pb3-Pb4'], linestyle='-.', label='SS-T2-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='>')
plt.plot(t1['Time in Minutes'],t1['Average-Pb4'], label='T1-Pb4', color='C6',  markevery=10, ms=4, marker='<')
plt.plot(t4['Time in Minutes'],t4['Average-Pb4'], linestyle='--', label='T4-Pb4', color='C6',  markevery=10, ms=4, marker='|')
plt.plot(sst1['Time in Minutes'],sst1['Average-Pb4'], linestyle=':', label='SS-T1-Pb4', color='C6',  markevery=10, ms=4, marker='8')
plt.plot(sst2['Time in Minutes'],sst2['Average-Pb4'], linestyle='-.', label='SS-T2-Pb4', color='C6',  markevery=10, ms=4, marker='^')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.gcf()
plt.savefig('T1vsT4vSS-T1vsSS-T2-Avg-Pb.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Fire-HF'], label='T1-Stud3-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t4['Time in Minutes'],t4['Stud3-Top-Fire-HF'], label='T4-Stud3-Top-Fire-HF', color='red', markevery=4, ms=4, marker='v', linestyle='--')
plt.plot(sst1['Time in Minutes'],sst1['Stud4-Mid-HF'], linestyle=':', label='SS-T1-Stud4-Mid-HF', color='red', markevery=10, ms=4, marker='s')
plt.plot(sst2['Time in Minutes'],sst2['Stud4-Top-HF'], linestyle='-.', label='SS-T2-Stud4-Top-HF', color='red', markevery=10, ms=4, marker='d')
plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Fire-CF'], label='T1-Stud3-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='x')
plt.plot(t4['Time in Minutes'],t4['Stud3-Top-Fire-CF'], label='T4-Stud3-Top-Fire-CF', color='C0', markevery=4, ms=4, marker='p', linestyle='--')
plt.plot(sst1['Time in Minutes'],sst1['Stud4-Mid-CF'], linestyle=':', label='SS-T1-Stud4-Mid-CF', color='C0', markevery=10, ms=4, marker='h')
plt.plot(sst2['Time in Minutes'],sst2['Stud4-Top-CF'], linestyle='-.', label='SS-T2-Stud4-Top-CF', color='C0', markevery=10, ms=4, marker='d')
plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Amb-HF'], label='T1-Stud3-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='+')
plt.plot(t4['Time in Minutes'],t4['Stud3-Top-Amb-HF'], label='T4-Stud3-Top-Amb-HF', color='C1', markevery=4, ms=4, marker='1', linestyle='--')
plt.plot(t1['Time in Minutes'],t1['Stud3-Top-Amb-CF'], label='T1-Stud3-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='*')
plt.plot(t4['Time in Minutes'],t4['Stud3-Top-Amb-CF'], label='T4-Stud3-Top-Amb-CF', color='C2', markevery=4, ms=4, marker='X', linestyle='--')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1vsT4vSS-T1vsSS-T2-Studs.pdf', bbox_inches='tight')
plt.show()
