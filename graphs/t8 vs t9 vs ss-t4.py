import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
t8 = pd.read_csv('t8.csv')
t9 = pd.read_csv('t9.csv')
sst4 = pd.read_csv('ss-t4.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t8['Time in Minutes'],t8['Average-Pb1'], label='T8-Pb1', color='red',  markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Average-Pb1'], linestyle='--', label='T9-Pb1', color='red',  markevery=10, ms=4, marker='v')
plt.plot(sst4['Time in Minutes'],sst4['Average-Pb1'], linestyle=':', label='SS-T4-Pb1', color='red',  markevery=10, ms=4, marker='s')
plt.plot(t8['Time in Minutes'],t8['Average-Pb1-Pb2'], label='T8-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='x')
plt.plot(t9['Time in Minutes'],t9['Average-Pb1-Pb2'], linestyle='--', label='T9-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='p')
plt.plot(sst4['Time in Minutes'],sst4['Average-Pb1-Pb2'], linestyle=':', label='SS-T4-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='x')
plt.plot(t8['Time in Minutes'],t8['Average-Pb2'], label='T8-Pb2', color='C1',  markevery=10, ms=4, marker='h')
plt.plot(t9['Time in Minutes'],t9['Average-Pb2'], linestyle='--', label='T9-Pb2', color='C1',  markevery=10, ms=4, marker='1')
plt.plot(sst4['Time in Minutes'],sst4['Average-Pb2'], linestyle=':', label='SS-T4-Pb2', color='C1',  markevery=10, ms=4, marker='+')
plt.plot(t8['Time in Minutes'],t8['Average-Pb3-Fire'], label='T8-Pb3-Fire', color='C7',  markevery=10, ms=4, marker='P')
plt.plot(t8['Time in Minutes'],t8['Average-Pb3-Amb'], label='T8-Pb3-Amb', color='C8',  markevery=10, ms=4, marker='P')
plt.plot(t8['Time in Minutes'],t8['Average-Pb4'], label='T8-Pb4', color='C2',  markevery=10, ms=4, marker='P')
plt.plot(t9['Time in Minutes'],t9['Average-Pb3'], linestyle='--', label='T9-Pb3', color='C2',  markevery=10, ms=4, marker='X')
plt.plot(sst4['Time in Minutes'],sst4['Average-Pb3'], linestyle=':', label='SS-T4-Pb3', color='C2',  markevery=10, ms=4, marker='D')
plt.plot(t8['Time in Minutes'],t8['Average-Pb4-Pb5'], label='T8-Pb4-Pb5', color='C4',  markevery=10, ms=4, marker='2')
plt.plot(t9['Time in Minutes'],t9['Average-Pb3-Pb4'], linestyle='--', label='T9-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='3')
plt.plot(sst4['Time in Minutes'],sst4['Average-Pb3-Pb4'], linestyle=':', label='SS-T4-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='4')
plt.plot(t8['Time in Minutes'],t8['Average-Pb5'], label='T8-Pb5', color='C6',  markevery=10, ms=4, marker='<')
plt.plot(t9['Time in Minutes'],t9['Average-Pb4'], linestyle='--', label='T9-Pb4', color='C6',  markevery=10, ms=4, marker='|')
plt.plot(sst4['Time in Minutes'],sst4['Average-Pb4'], linestyle=':', label='SS-T4-Pb4', color='C6',  markevery=10, ms=4, marker='8')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.gcf()
plt.savefig('T8vsT9vSS-T4-Avg-Pb.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t8['Time in Minutes'],t8['Stud3-Mid-Fire-HF'], label='T8-Stud3-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Fire-HF'], label='T9-Stud4-Mid-Fire-HF', color='red', markevery=4, ms=4, marker='v', linestyle='--')
plt.plot(sst4['Time in Minutes'],sst4['Stud4-Mid-HF'], linestyle=':', label='SS-T4-Stud4-Mid-HF', color='red', markevery=10, ms=4, marker='s')
plt.plot(t8['Time in Minutes'],t8['Stud3-Mid-Fire-CF'], label='T8-Stud3-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='x')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Fire-CF'], label='T9-Stud4-Mid-Fire-CF', color='C0', markevery=4, ms=4, marker='p', linestyle='--')
plt.plot(sst4['Time in Minutes'],sst4['Stud4-Mid-CF'], linestyle=':', label='SS-T4-Stud4-Mid-CF', color='C0', markevery=10, ms=4, marker='h')
plt.plot(t8['Time in Minutes'],t8['Stud3-Mid-Amb-HF'], label='T8-Stud3-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='+')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Amb-HF'], label='T9-Stud4-Mid-Amb-HF', color='C1', markevery=4, ms=4, marker='1', linestyle='--')
plt.plot(t8['Time in Minutes'],t8['Stud3-Mid-Amb-CF'], label='T8-Stud3-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='*')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Amb-CF'], label='T9-Stud4-Mid-Amb-CF', color='C2', markevery=4, ms=4, marker='X', linestyle='--')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8vsT9vSS-T4-Studs.pdf', bbox_inches='tight')
plt.show()
