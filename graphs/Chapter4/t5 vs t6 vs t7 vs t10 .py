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
t6 = pd.read_csv('t6.csv')
t7 = pd.read_csv('t7.csv')
t10 = pd.read_csv('t10.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,100])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t5['Time in Minutes'],t5['Average-Pb1'], label='T5-Pb1', color='red',  markevery=10, ms=4, marker='o')
plt.plot(t6['Time in Minutes'],t6['Average-Pb1'], linestyle='-.', label='T6-Pb1', color='red',  markevery=10, ms=4, marker='v')
plt.plot(t7['Time in Minutes'],t7['Average-Pb1'], linestyle='--', label='T7-Pb1', color='red',  markevery=10, ms=4, marker='s')
plt.plot(t10['Time in Minutes'],t10['Average-Pb1'], linestyle=':', label='T10-Pb1', color='red',  markevery=200, ms=4, marker='^')
plt.plot(t5['Time in Minutes'],t5['Average-Pb1-Pb2'], label='T5-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='d')
plt.plot(t6['Time in Minutes'],t6['Average-Pb1-Pb2'], linestyle='-.', label='T6-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='>')
plt.plot(t7['Time in Minutes'],t7['Average-Pb1-Pb2'], linestyle='--', label='T7-Pb1-Pb2', color='C0',  markevery=10, ms=4, marker='+')
plt.plot(t10['Time in Minutes'],t10['Average-Pb1-Pb2'], linestyle=':', label='T10-Pb1-Pb2', color='C0',  markevery=200, ms=4, marker='>')
plt.plot(t5['Time in Minutes'],t5['Average-Pb2'], label='T5-Pb2', color='C1',  markevery=10, ms=4, marker='1')
plt.plot(t6['Time in Minutes'],t6['Average-Pb2'], linestyle='-.', label='T6-Pb2', color='C1',  markevery=10, ms=4, marker='h')
plt.plot(t7['Time in Minutes'],t7['Average-Pb2'], linestyle='--', label='T7-Pb2', color='C1',  markevery=10, ms=4, marker='p')
plt.plot(t10['Time in Minutes'],t10['Average-Pb2'], linestyle=':', label='T10-Pb2', color='C1',  markevery=200, ms=4, marker='<')
plt.plot(t5['Time in Minutes'],t5['Average-Pb3'], label='T5-Pb3', color='C2',  markevery=10, ms=4, marker='P')
plt.plot(t6['Time in Minutes'],t6['Average-Pb3'], linestyle='-.', label='T6-Pb3', color='C2',  markevery=10, ms=4, marker='x')
plt.plot(t7['Time in Minutes'],t7['Average-Pb3'], linestyle='--', label='T7-Pb3', color='C2',  markevery=10, ms=4, marker='X')
plt.plot(t10['Time in Minutes'],t10['Average-Pb3'], linestyle=':', label='T10-Pb3', color='C2',  markevery=200, ms=4, marker='2')
plt.plot(t5['Time in Minutes'],t5['Average-Pb3-Pb4'], label='T5-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='*')
plt.plot(t6['Time in Minutes'],t6['Average-Pb3-Pb4'], linestyle='-.', label='T6-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker='|')
plt.plot(t7['Time in Minutes'],t7['Average-Pb3-Pb4'], linestyle='--', label='T7-Pb3-Pb4', color='C4',  markevery=10, ms=4, marker=4)
plt.plot(t10['Time in Minutes'],t10['Average-Pb3-Pb4'], linestyle=':', label='T7-Pb3-Pb4', color='C4',  markevery=200, ms=4, marker=8)
plt.plot(t5['Time in Minutes'],t5['Average-Pb4'], label='T5-Pb4', color='C6',  markevery=10, ms=4, marker=5)
plt.plot(t6['Time in Minutes'],t6['Average-Pb4'], linestyle='-.', label='T6-Pb4', color='C6',  markevery=10, ms=4, marker='D')
plt.plot(t7['Time in Minutes'],t7['Average-Pb4'], linestyle='--', label='T7-Pb4', color='C6',  markevery=10, ms=4, marker='H')
plt.plot(t10['Time in Minutes'],t10['Average-Pb4'], linestyle=':', label='T10-Pb4', color='C6',  markevery=200, ms=4, marker='_')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.gcf()
plt.savefig('T5vsT6vsT7vsT10-Avg-Pb.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t5['Time in Minutes'],t5['Stud4-Mid-Fire-HF'], label='T5-Stud4-Mid-Fire-HF', color='red', markevery=5, ms=4, marker='o')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-HF'], label='T6-Stud3-Top-Fire-HF', color='red', markevery=5, ms=4, marker='x', linestyle='--')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Fire-HF'], label='T7-Stud3-Mid-Fire-HF', color='red', markevery=5, ms=4, marker='h', linestyle='-.')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Fire-HF'], label='T10-Stud3-Top-Fire-HF', color='red', markevery=1000, ms=4, marker='8', linestyle=':')
plt.plot(t5['Time in Minutes'],t5['Stud4-Mid-Fire-CF'], label='T5-Stud4-Mid-Fire-CF', color='C0', markevery=5, ms=4, marker='v')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-CF'], label='T6-Stud3-Top-Fire-CF', color='C0', markevery=5, ms=4, marker='p', linestyle='--')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Fire-CF'], label='T7-Stud3-Mid-Fire-CF', color='C0', markevery=5, ms=4, marker='H', linestyle='-.')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Fire-CF'], label='T10-Stud3-Top-Fire-CF', color='C0', markevery=1000, ms=4, marker='D', linestyle=':')
plt.plot(t5['Time in Minutes'],t5['Stud4-Mid-Amb-HF'], label='T5-Stud4-Mid-Amb-HF', color='C1', markevery=5, ms=4, marker='s')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-HF'], label='T6-Stud3-Top-Amb-HF', color='C1', markevery=5, ms=4, marker='+', linestyle='--')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Amb-HF'], label='T7-Stud3-Mid-Amb-HF', color='C1', markevery=5, ms=4, marker='P', linestyle='-.')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Amb-HF'], label='T10-Stud3-Top-Amb-HF', color='C1', markevery=1000, ms=4, marker='1', linestyle=':')
plt.plot(t5['Time in Minutes'],t5['Stud4-Mid-Amb-CF'], label='T5-Stud4-Mid-Amb-CF', color='C2', markevery=5, ms=4, marker='d')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-CF'], label='T6-Stud3-Top-Amb-CF', color='C2', markevery=5, ms=4, marker='*', linestyle='--')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid-Amb-CF'], label='T7-Stud3-Mid-Amb-CF', color='C2', markevery=5, ms=4, marker='X', linestyle='-.')
plt.plot(t10['Time in Minutes'],t10['Stud3-Top-Amb-CF'], label='T10-Stud3-Top-Amb-CF', color='C2', markevery=1000, ms=4, marker='|', linestyle=':')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T5vsT6vsT7vsT10-Studs.pdf', bbox_inches='tight')
plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-HF'], label='T5-Stud3-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-HF'], linestyle='--', label='T6-Stud3-Fire-HF', color='red')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Fire-CF'], label='T5-Stud3-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-CF'], linestyle='--', label='T6-Stud3-Fire-CF', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-HF'], label='T5-Stud3-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-HF'], linestyle='--', label='T6-Stud3-Amb-HF', color='C1')
#plt.plot(t5['Time in Minutes'],t5['Stud3-Top-Amb-CF'], label='T5-Stud3-Amb-CF', color='C2')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-CF'], linestyle='--', label='T6-Stud3-Amb-CF', color='C2')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT6-Studs.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], label='T5-Stud3-Axial', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Axial'], linestyle='--', label='T6-Stud3-Axial', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud4-Axial'], label='T5-Stud4-Axial', color='C3')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Axial'], linestyle='--', label='T6-Stud4-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT6-Axial.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], label='T5-Stud3-Axial', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Axial'], linestyle='--', label='T6-Stud3-Axial', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud5-Axial'], label='T5-Stud5-Axial', color='C3')
#plt.plot(t6['Time in Minutes'],t6['Stud5-Axial'], linestyle='--', label='T6-Stud5-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT6-Axial2.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Stud3-Mid'], label='T5-Stud3-Lateral', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Mid'], linestyle='--', label='T6-Stud3-Lateral', color='C0')
#plt.plot(t5['Time in Minutes'],t5['Stud4-Mid'], label='T5-Stud4-Lateral', color='C3')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Mid'], linestyle='--', label='T6-Stud4-Lateral', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Lateral Deflection(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT6-Lateral.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t5['Time in Minutes'],t5['Load in kN'], label='T5-Load', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Load in kN'], linestyle='--', label='T6-Load', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Applied Axial Load(kN)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T5vsT6-Load.pdf', bbox_inches='tight')
#plt.show()