import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
t5 = pd.read_csv('t5.csv')
t7 = pd.read_csv('t7.csv')
t10 = pd.read_csv('t10.csv')
sst3 = pd.read_csv('ss-t3.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,120])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t5['Time in Minutes'],t5['Average-Pb1'], label='T5-Pb1', color='red',  markevery=10, ms=4, marker='o')
plt.plot(t7['Time in Minutes'],t7['Average-Pb1'], linestyle='--', label='T7-Pb1', color='red',  markevery=10, ms=4, marker='v')
plt.plot(t10['Time in Minutes'],t10['Average-Pb1'], linestyle=':', label='T10-Pb1', color='red',  markevery=200, ms=4, marker='s')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb1'], linestyle='-.', label='SS-T3-Pb1', color='red', markevery=10, ms=4, marker='d')
plt.plot(t5['Time in Minutes'],t5['Average-Pb1-Pb2'], label='T5-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='x')
plt.plot(t7['Time in Minutes'],t7['Average-Pb1-Pb2'], linestyle='--', label='T7-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='p')
plt.plot(t10['Time in Minutes'],t10['Average-Pb1-Pb2'], linestyle=':', label='T10-Pb1-Pb2', color='C0',  markevery=200, ms=4, marker='h')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb1-Pb2'], linestyle='-.', label='SS-T3-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='*')
plt.plot(t5['Time in Minutes'],t5['Average-Pb2'], label='T5-Pb2', color='C1',  markevery=10, ms=4, marker='+')
plt.plot(t7['Time in Minutes'],t7['Average-Pb2'], linestyle='--', label='T7-Pb2', color='C1',  markevery=10, ms=4, marker='X')
plt.plot(t10['Time in Minutes'],t10['Average-Pb2'], linestyle=':', label='T10-Pb2', color='C1',  markevery=200, ms=4, marker='D')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb2'], linestyle='-.', label='SS-T3-Pb2', color='C1', markevery=10, ms=4, marker='H')
plt.plot(t5['Time in Minutes'],t5['Average-Pb3'], label='T5-Pb3', color='C2',  markevery=10, ms=4, marker='$y$')
plt.plot(t7['Time in Minutes'],t7['Average-Pb3'], linestyle='--', label='T7-Pb3', color='C2',  markevery=10, ms=4, marker='8')
plt.plot(t10['Time in Minutes'],t10['Average-Pb3'], linestyle=':', label='T10-Pb3', color='C2',  markevery=200, ms=4, marker='P')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb3'], linestyle='-.', label='SS-T3-Pb3', color='C2', markevery=10, ms=4, marker='^')
plt.plot(t5['Time in Minutes'],t5['Average-Pb3-Pb4'], label='T5-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='<')
plt.plot(t7['Time in Minutes'],t7['Average-Pb3-Pb4'], linestyle='--', label='T7-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='>')
plt.plot(t10['Time in Minutes'],t10['Average-Pb3-Pb4'], linestyle=':', label='T7-Pb3-Pb4', color='C4',  markevery=200, ms=4, marker='|')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb3-Pb4'], linestyle='-.', label='SS-T3-Pb3-Pb4', color='C4', markevery=10, ms=4, marker='$o$')
plt.plot(t5['Time in Minutes'],t5['Average-Pb4'], label='T5-Pb4', color='C6',  markevery=10, ms=4, marker='$N$')
plt.plot(t7['Time in Minutes'],t7['Average-Pb4'], linestyle='--', label='T7-Pb4', color='C6',  markevery=10, ms=4, marker='H')
plt.plot(t10['Time in Minutes'],t10['Average-Pb4'], linestyle=':', label='T10-Pb4', color='C6',  markevery=200, ms=4, marker='$a$')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb4'], linestyle='-.', label='SS-T3-Pb4', color='C6', markevery=10, ms=4, marker='$b$')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T5vsT7vsT10vsSS-T3-Avg-Pb.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-HF'], label='T5-Stud3-Top-Fire-HF', color='red', markevery=5, ms=4, marker='o')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Fire-HF'], label='T7-Stud3-Mid-Fire-HF', color='red', markevery=5, ms=4, marker='v', linestyle='--')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Fire-HF'], label='T10-Stud3-Top-Fire-HF', color='red', markevery=1000, ms=4, marker='s', linestyle=':')
plt.plot(sst3['Time in Minutes'],sst3['Stud2-Mid-HF'], label='SS-T3-Stud2-Mid-HF', color='red', markevery=10, ms=4, marker='d', linestyle='-.')
plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-CF'], label='T5-Stud3-Top-Fire-CF', color='C0', markevery=5, ms=4, marker='x')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Fire-CF'], label='T7-Stud3-Mid-Fire-CF', color='C0', markevery=5, ms=4, marker='p', linestyle='--')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Fire-CF'], label='T10-Stud3-Top-Fire-CF', color='C0', markevery=1000, ms=4, marker='h', linestyle=':')
plt.plot(sst3['Time in Minutes'],sst3['Stud2-Mid-CF'], label='SS-T3-Stud2-Mid-CF', color='C0', markevery=10, ms=4, marker='*', linestyle='-.')
plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-HF'], label='T5-Stud3-Top-Amb-HF', color='C1', markevery=5, ms=4, marker='+')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Amb-HF'], label='T7-Stud3-Mid-Amb-HF', color='C1', markevery=5, ms=4, marker='P', linestyle='--')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Amb-HF'], label='T10-Stud3-Top-Amb-HF', color='C1', markevery=1000, ms=4, marker='X', linestyle=':')
plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-CF'], label='T5-Stud3-Top-Amb-CF', color='C2', markevery=5, ms=4, marker='D')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Amb-CF'], label='T7-Stud3-Mid-Amb-CF', color='C2', markevery=5, ms=4, marker='^', linestyle='--')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Amb-CF'], label='T10-Stud3-Top-Amb-CF', color='C2', markevery=1000, ms=4, marker='<', linestyle=':')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T5vsT7vsT10vsSS-T3-Studs.pdf', bbox_inches='tight')
plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-HF'], label='T5-Stud3-Fire-HF', color='red')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-HF'], linestyle='--', label='T5-Stud3-Fire-HF', color='red')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-CF'], label='T5-Stud3-Fire-CF', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-CF'], linestyle='--', label='T5-Stud3-Fire-CF', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-HF'], label='T5-Stud3-Amb-HF', color='C1')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-HF'], linestyle='--', label='T5-Stud3-Amb-HF', color='C1')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-CF'], label='T5-Stud3-Amb-CF', color='C2')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-CF'], linestyle='--', label='T5-Stud3-Amb-CF', color='C2')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT5-Studs.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], label='T5-Stud3-Axial', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], linestyle='--', label='T5-Stud3-Axial', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud4-Axial'], label='T5-Stud4-Axial', color='C3')
#plt.plot(t5['Time in Minutes'],t5['Stud4-Axial'], linestyle='--', label='T5-Stud4-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT5-Axial.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], label='T5-Stud3-Axial', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], linestyle='--', label='T5-Stud3-Axial', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud5-Axial'], label='T5-Stud5-Axial', color='C3')
#plt.plot(t5['Time in Minutes'],t5['Stud5-Axial'], linestyle='--', label='T5-Stud5-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT5-Axial2.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Mid'], label='T5-Stud3-Lateral', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Mid'], linestyle='--', label='T5-Stud3-Lateral', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud4-Mid'], label='T5-Stud4-Lateral', color='C3')
#plt.plot(t5['Time in Minutes'],t5['Stud4-Mid'], linestyle='--', label='T5-Stud4-Lateral', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Lateral Deflection(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT5-Lateral.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Load in kN'], label='T5-Load', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Load in kN'], linestyle='--', label='T5-Load', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Applied Axial Load(kN)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT5-Load.pdf', bbox_inches='tight')
#plt.show()