import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
T1 = pd.read_csv('t1.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,180])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(T1['Time in Minutes'],T1['Average-Furnace'], label='T1-Furnace', color='maroon')
plt.plot(T1['Time in Minutes'],T1['Average-Pb1'], label='T1-Pb1', color='red', markevery=10, ms=4, marker='o')
plt.plot(T1['Time in Minutes'],T1['Average-Pb1-Pb2'], label='T1-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T1['Time in Minutes'],T1['Average-Pb2'], label='T1-Pb2', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T1['Time in Minutes'],T1['Average-Pb3'], label='T1-Pb3', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T1['Time in Minutes'],T1['Average-Pb3-Pb4'], label='T1-Pb3-Pb4', color='C4', markevery=10, ms=4, marker='>')
plt.plot(T1['Time in Minutes'],T1['Average-Pb4'], label='T1-Pb4', color='C6', markevery=10, ms=4, marker='+')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-Plasterboard.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T1['Time in Minutes'],T1['Stud3-Top-Fire-HF'], label='T1-Stud3-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(T1['Time in Minutes'],T1['Stud3-Top-Fire-CF'], label='T1-Stud3-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T1['Time in Minutes'],T1['Stud3-Top-Amb-HF'], label='T1-Stud3-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T1['Time in Minutes'],T1['Stud3-Top-Amb-CF'], label='T1-Stud3-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T1['Time in Minutes'],T1['Stud4-Top-Fire-HF'], label='T1-Stud4-Top-Fire-HF', color='red', markevery=10, ms=4, marker='>', linestyle='--')
plt.plot(T1['Time in Minutes'],T1['Stud4-Top-Fire-CF'], label='T1-Stud4-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='p', linestyle='--')
plt.plot(T1['Time in Minutes'],T1['Stud4-Top-Amb-HF'], label='T1-Stud4-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='*', linestyle='--')
plt.plot(T1['Time in Minutes'],T1['Stud4-Top-Amb-CF'], label='T1-Stud4-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='x', linestyle='--')
plt.xlabel('Time(min)')
plt.ylabel('Temperature(°C)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-Stud3-4-Top.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T1['Time in Minutes'],T1['Stud2-Axial'], label='T1-Stud2-Axial', color='red', markevery=10, ms=4, marker='o')
plt.plot(T1['Time in Minutes'],T1['Stud3-Axial'], label='T1-Stud3-Axial', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T1['Time in Minutes'],T1['Stud4-Axial'], label='T1-Stud4-Axial', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T1['Time in Minutes'],T1['Stud5-Axial'], label='T1-Stud5-Axial', color='C2', markevery=10, ms=4, marker='d')
plt.xlabel('Time(min)')
plt.ylabel('Axial Displacement(mm)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-Axial.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T1['Time in Minutes'],T1['Stud3-Top'], label='T1-Stud3-Top', color='red', markevery=10, ms=4, marker='o')
plt.plot(T1['Time in Minutes'],T1['Stud3-Mid'], label='T1-Stud3-Mid', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T1['Time in Minutes'],T1['Stud3-Bottom'], label='T1-Stud3-Bottom', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T1['Time in Minutes'],T1['Stud4-Top'], label='T1-Stud4-Top', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T1['Time in Minutes'],T1['Stud4-Mid'], label='T1-Stud4-Mid', color='C4', markevery=10, ms=4, marker='>')
plt.plot(T1['Time in Minutes'],T1['Stud4-Bottom'], label='T1-Stud4-Bottom', color='C6', markevery=10, ms=4, marker='+')
plt.xlabel('Time(min)')
plt.ylabel('Lateral Deflection(mm)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1-Lateral.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_ylim([0,40])
plt.plot(T1['Time in Minutes'],T1['Load in kN'], label='T1-Applied Axial Load', color='C0', markevery=10, ms=4, marker='o')
plt.xlabel('Time(min)')
plt.ylabel('Applied Axial Load(kN)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T1-Load.pdf', bbox_inches='tight')
plt.show()