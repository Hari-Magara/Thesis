import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
T8 = pd.read_csv('T8.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,250])
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(T8['Time in Minutes'],T8['Average-Furnace'], label='T8-Furnace', color='maroon')
plt.plot(T8['Time in Minutes'],T8['Average-Pb1'], label='T8-Pb1', color='red', markevery=10, ms=4, marker='o')
plt.plot(T8['Time in Minutes'],T8['Average-Pb1-Pb2'], label='T8-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T8['Time in Minutes'],T8['Average-Pb2'], label='T8-Pb2', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T8['Time in Minutes'],T8['Average-Pb3-Fire'], label='T8-Pb3-Fire', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T8['Time in Minutes'],T8['Average-Pb3-Amb'], label='T8-Pb3-Amb', color='C3', markevery=10, ms=4, marker='>')
plt.plot(T8['Time in Minutes'],T8['Average-Pb4'], label='T8-Pb4', color='C4', markevery=10, ms=4, marker='p')
plt.plot(T8['Time in Minutes'],T8['Average-Pb4-Pb5'], label='T8-Pb4-Pb5', color='C5', markevery=10, ms=4, marker='*')
plt.plot(T8['Time in Minutes'],T8['Average-Pb5'], label='T8-Pb5', color='C6', markevery=10, ms=4, marker='+')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-Plasterboard.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,250])
#ax.set_ylim([0,120])
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T8['Time in Minutes'],T8['Pb5-Top-Left'], label='T8-Pb5-Top-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(T8['Time in Minutes'],T8['Pb5-Top-Right'], label='T8-Pb5-Top-Right', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T8['Time in Minutes'],T8['Pb5-Mid-Mid'], label='T8-Pb5-Mid-Mid', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T8['Time in Minutes'],T8['Pb5-Bottom-Left'], label='T8-Pb5-Bottom-Left', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T8['Time in Minutes'],T8['Pb5-Bottom-Right'], label='T8-Pb5-Bottom-Right', color='C4', markevery=10, ms=4, marker='>')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-Plasterboard-5.pdf', bbox_inches='tight')
plt.show()


ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,250])
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T8['Time in Minutes'],T8['Stud3-Mid-Fire-HF'], label='T8-Stud3-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(T8['Time in Minutes'],T8['Stud3-Mid-Fire-CF'], label='T8-Stud3-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T8['Time in Minutes'],T8['Stud3-Mid-Amb-HF'], label='T8-Stud3-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T8['Time in Minutes'],T8['Stud3-Mid-Amb-CF'], label='T8-Stud3-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T8['Time in Minutes'],T8['Stud4-Mid-Fire-HF'], label='T8-Stud4-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='>', linestyle='--')
plt.plot(T8['Time in Minutes'],T8['Stud4-Mid-Fire-CF'], label='T8-Stud4-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='p', linestyle='--')
plt.plot(T8['Time in Minutes'],T8['Stud4-Mid-Amb-HF'], label='T8-Stud4-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='*', linestyle='--')
plt.plot(T8['Time in Minutes'],T8['Stud4-Mid-Amb-CF'], label='T8-Stud4-Mid-Amb-HF', color='C2', markevery=10, ms=4, marker='+', linestyle='--')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-Studs-3-4-Mid.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T8['Time in Minutes'],T8['Stud3-Axial'], label='T8-Stud3-Axial', color='red', markevery=10, ms=4, marker='o')
plt.plot(T8['Time in Minutes'],T8['Stud4-Axial'], label='T8-Stud4-Axial', color='C0', markevery=10, ms=4, marker='v')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Axial Displacement(mm)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-Axial.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(T8['Time in Minutes'],T8['Stud2-Mid'], label='T8-Stud2-Mid', color='red', markevery=10, ms=4, marker='o')
plt.plot(T8['Time in Minutes'],T8['Stud3-Top'], label='T8-Stud3-Top', color='C0', markevery=10, ms=4, marker='v')
plt.plot(T8['Time in Minutes'],T8['Stud3-Mid'], label='T8-Stud3-Mid', color='C1', markevery=10, ms=4, marker='s')
plt.plot(T8['Time in Minutes'],T8['Stud3-Bottom'], label='T8-Stud3-Bottom', color='C2', markevery=10, ms=4, marker='d')
plt.plot(T8['Time in Minutes'],T8['Stud4-Top'], label='T8-Stud4-Top', color='C4', markevery=10, ms=4, marker='>')
plt.plot(T8['Time in Minutes'],T8['Stud4-Mid'], label='T8-Stud4-Mid', color='C6', markevery=10, ms=4, marker='p')
plt.plot(T8['Time in Minutes'],T8['Stud4-Bottom'], label='T8-Stud4-Bottom', color='C7', markevery=10, ms=4, marker='*')
plt.plot(T8['Time in Minutes'],T8['Stud5-Mid'], label='T8-Stud5-Mid', color='C8', markevery=10, ms=4, marker='+')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Lateral Deflection(mm)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T8-Lateral.pdf', bbox_inches='tight')
plt.show()