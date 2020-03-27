import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
T6 = pd.read_csv('T6.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,100])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(T6['Time in Minutes'],T6['Average-Furnace'], label='T6-Furnace', color='maroon')
plt.plot(T6['Time in Minutes'],T6['Average-Pb1'], label='T6-Pb1', color='red', markevery=5, ms=4, marker='o')
plt.plot(T6['Time in Minutes'],T6['Average-Pb1-Pb2'], label='T6-Pb1-Pb2', color='C0', markevery=5, ms=4, marker='v')
plt.plot(T6['Time in Minutes'],T6['Average-Pb2'], label='T6-Pb2', color='C1', markevery=5, ms=4, marker='s')
plt.plot(T6['Time in Minutes'],T6['Average-Pb3'], label='T6-Pb3', color='C2', markevery=5, ms=4, marker='d')
plt.plot(T6['Time in Minutes'],T6['Average-Pb3-Pb4'], label='T6-Pb3-Pb4', color='C4', markevery=5, ms=4, marker='>')
plt.plot(T6['Time in Minutes'],T6['Average-Pb4'], label='T6-Pb4', color='C6', markevery=5, ms=4, marker='+')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T6-Plasterboard.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T6['Time in Minutes'],T6['Stud3-Top-Fire-HF'], label='T6-Stud3-Top-Fire-HF', color='red', markevery=5, ms=4, marker='o')
plt.plot(T6['Time in Minutes'],T6['Stud3-Top-Fire-CF'], label='T6-Stud3-Top-Fire-CF', color='C0', markevery=5, ms=4, marker='v')
plt.plot(T6['Time in Minutes'],T6['Stud3-Top-Amb-HF'], label='T6-Stud3-Top-Amb-HF', color='C1', markevery=5, ms=4, marker='s')
plt.plot(T6['Time in Minutes'],T6['Stud3-Top-Amb-CF'], label='T6-Stud3-Top-Amb-CF', color='C2', markevery=5, ms=4, marker='d')
plt.plot(T6['Time in Minutes'],T6['Stud4-Top-Fire-HF'], label='T6-Stud4-Top-Fire-HF', color='red', markevery=5, ms=4, marker='>', linestyle='--')
plt.plot(T6['Time in Minutes'],T6['Stud4-Top-Fire-CF'], label='T6-Stud4-Top-Fire-CF', color='C0', markevery=5, ms=4, marker='p', linestyle='--')
plt.plot(T6['Time in Minutes'],T6['Stud4-Top-Amb-HF'], label='T6-Stud4-Top-Amb-HF', color='C1', markevery=5, ms=4, marker='*', linestyle='--')
plt.plot(T6['Time in Minutes'],T6['Stud4-Top-Amb-CF'], label='T6-Stud4-Top-Amb-CF', color='C2', markevery=5, ms=4, marker='x', linestyle='--')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T6-Stud3-4-Top.pdf', bbox_inches='tight')
plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(T6['Time in Minutes'],T6['Stud3-Mid-Fire-HF'], label='T6-Stud3-Mid-Fire-HF', color='red', markevery=5, ms=4, marker='o')
#plt.plot(T6['Time in Minutes'],T6['Stud3-Mid-Fire-CF'], label='T6-Stud3-Mid-Fire-CF', color='C0', markevery=5, ms=4, marker='v')
#plt.plot(T6['Time in Minutes'],T6['Stud3-Mid-Amb-HF'], label='T6-Stud3-Mid-Amb-HF', color='C1', markevery=5, ms=4, marker='s')
#plt.plot(T6['Time in Minutes'],T6['Stud3-Mid-Amb-CF'], label='T6-Stud3-Mid-Amb-CF', color='C2', markevery=5, ms=4, marker='d')
#plt.plot(T6['Time in Minutes'],T6['Stud4-Mid-Fire-HF'], label='T6-Stud4-Mid-Fire-HF', color='red', markevery=5, ms=4, marker='>', linestyle='--')
#plt.plot(T6['Time in Minutes'],T6['Stud4-Mid-Fire-CF'], label='T6-Stud4-Mid-Fire-CF', color='C0', markevery=5, ms=4, marker='p', linestyle='--')
#plt.plot(T6['Time in Minutes'],T6['Stud4-Mid-Amb-HF'], label='T6-Stud4-Mid-Amb-HF', color='C1', markevery=5, ms=4, marker='*', linestyle='--')
#plt.plot(T6['Time in Minutes'],T6['Stud4-Mid-Amb-CF'], label='T6-Stud4-Mid-Amb-CF', color='C2', markevery=5, ms=4, marker='x', linestyle='--')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('T6-Stud3-4-Mid.pdf', bbox_inches='tight')
#plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T6['Time in Minutes'],T6['Stud2-Axial'], label='T6-Stud2-Axial', color='red', markevery=5, ms=4, marker='o')
plt.plot(T6['Time in Minutes'],T6['Stud3-Axial'], label='T6-Stud3-Axial', color='C0', markevery=5, ms=4, marker='v')
plt.plot(T6['Time in Minutes'],T6['Stud4-Axial'], label='T6-Stud4-Axial', color='C1', markevery=5, ms=4, marker='s')
plt.plot(T6['Time in Minutes'],T6['Stud5-Axial'], label='T6-Stud5-Axial', color='C2', markevery=5, ms=4, marker='d')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Axial Displacement(mm)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T6-Axial.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T6['Time in Minutes'],T6['Stud3-Top'], label='T6-Stud3-Top', color='red', markevery=5, ms=4, marker='o')
plt.plot(T6['Time in Minutes'],T6['Stud3-Mid'], label='T6-Stud3-Mid', color='C0', markevery=5, ms=4, marker='v')
plt.plot(T6['Time in Minutes'],T6['Stud3-Bottom'], label='T6-Stud3-Bottom', color='C1', markevery=5, ms=4, marker='s')
plt.plot(T6['Time in Minutes'],T6['Stud4-Top'], label='T6-Stud4-Top', color='C2', markevery=5, ms=4, marker='d')
plt.plot(T6['Time in Minutes'],T6['Stud4-Mid'], label='T6-Stud4-Mid', color='C4', markevery=5, ms=4, marker='>')
plt.plot(T6['Time in Minutes'],T6['Stud4-Bottom'], label='T6-Stud4-Bottom', color='C6', markevery=5, ms=4, marker='+')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Lateral Deflection(mm)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T6-Lateral.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_ylim([0,50])
plt.plot(T6['Time in Minutes'],T6['Load in kN'], label='T6-Applied Axial Load', color='C0', markevery=5, ms=4, marker='o')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Applied Axial Load(kN)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T6-Load.pdf', bbox_inches='tight')
plt.show()