import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
ST1 = pd.read_csv('st1.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,180])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(ST1['Time in Minutes'],ST1['Average-Pb1'], label='ST1-Pb1', color='red', markevery=10, ms=4, marker='o')
plt.plot(ST1['Time in Minutes'],ST1['Average-Pb1-Pb2'], label='ST1-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='v')
plt.plot(ST1['Time in Minutes'],ST1['Average-Pb2'], label='ST1-Pb2', color='C1', markevery=10, ms=4, marker='s')
plt.plot(ST1['Time in Minutes'],ST1['Average-Pb3'], label='ST1-Pb3', color='C2', markevery=10, ms=4, marker='d')
plt.plot(ST1['Time in Minutes'],ST1['Average-Pb3-Pb4'], label='ST1-Pb3-Pb4', color='C4', markevery=10, ms=4, marker='>')
plt.plot(ST1['Time in Minutes'],ST1['Average-Pb4'], label='ST1-Pb4', color='C6', markevery=10, ms=4, marker='+')
#plt.title('ST1-Average Plasterboard')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('ST1-Average-Pb.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(ST1['Time in Minutes'],ST1['Stud1-Top-Fire-HF'], label='ST1-Stud1-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(ST1['Time in Minutes'],ST1['Stud1-Top-Fire-CF'], label='ST1-Stud1-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(ST1['Time in Minutes'],ST1['Stud1-Top-Amb-HF'], label='ST1-Stud1-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
# plt.plot(ST1['Time in Minutes'],ST1['Stud1-Top-Amb-CF'], label='ST1-Stud1-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Fire-HF'], label='ST1-Stud2-Top-Fire-HF', color='red', markevery=10, ms=4, marker='>', linestyle='--')
plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Fire-CF'], label='ST1-Stud2-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='p', linestyle='--')
plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Amb-HF'], label='ST1-Stud2-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='*', linestyle='--')
plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Amb-CF'], label='ST1-Stud2-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='+', linestyle='--')
#plt.title('ST1-Stud1-Mid')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('ST1-Stud1-2-Top.pdf', bbox_inches='tight')
plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(ST1['Time in Minutes'],ST1['Stud1-Bottom-Fire-HF'], label='ST1-Stud1-Bottom-Fire-HF', color='red', markevery=10, ms=4, marker='o')
#plt.plot(ST1['Time in Minutes'],ST1['Stud1-Bottom-Fire-CF'], label='ST1-Stud1-Bottom-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
#plt.plot(ST1['Time in Minutes'],ST1['Stud1-Bottom-Amb-HF'], label='ST1-Stud1-Bottom-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
#plt.plot(ST1['Time in Minutes'],ST1['Stud1-Bottom-Amb-CF'], label='ST1-Stud1-Bottom-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
##plt.title('ST1-Stud1-Mid')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('ST1-Stud1-Bottom.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Fire-HF'], label='ST1-Stud2-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Fire-CF'], label='ST1-Stud2-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Amb-HF'], label='ST1-Stud2-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Top-Amb-CF'], label='ST1-Stud2-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
##plt.title('ST1-Stud2-Mid')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('ST1-Stud2-Top.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Bottom-Fire-HF'], label='ST1-Stud2-Bottom-Fire-HF', color='red', markevery=10, ms=4, marker='o')
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Bottom-Fire-CF'], label='ST1-Stud2-Bottom-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Bottom-Amb-HF'], label='ST1-Stud2-Bottom-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
#plt.plot(ST1['Time in Minutes'],ST1['Stud2-Bottom-Amb-CF'], label='ST1-Stud2-Bottom-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
##plt.title('ST1-Stud2-Mid')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('ST1-Stud2-Bottom.pdf', bbox_inches='tight')
#plt.show()
