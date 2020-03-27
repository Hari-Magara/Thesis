import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
t6 = pd.read_csv('t6.csv')
sst3 = pd.read_csv('ss-t3.csv')

ax = plt.axes()      
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,120])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t6['Time in Minutes'],t6['Average-Pb1'], label='T6-Pb1', color='red', markevery=10, ms=4, marker='o')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb1'], linestyle='-.', label='SS-T3-Pb1', color='red', markevery=10, ms=4, marker='v')
plt.plot(t6['Time in Minutes'],t6['Average-Pb1-Pb2'], label='T6-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='s')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb1-Pb2'], linestyle='-.', label='SS-T3-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='d')
plt.plot(t6['Time in Minutes'],t6['Average-Pb2'], label='T6-Pb2', color='C1', markevery=10, ms=4, marker='>')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb2'], linestyle='-.', label='SS-T3-Pb2', color='C1', markevery=10, ms=4, marker='+')
plt.plot(t6['Time in Minutes'],t6['Average-Pb3'], label='T6-Pb3', color='C2', markevery=10, ms=4, marker='1')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb3'], linestyle='-.', label='SS-T3-Pb3', color='C2', markevery=10, ms=4, marker='h')
plt.plot(t6['Time in Minutes'],t6['Average-Pb3-Pb4'], label='T6-Pb3-Pb4', color='C4', markevery=10, ms=4, marker='p')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb3-Pb4'], linestyle='-.', label='SS-T3-Pb3-Pb4', color='C4', markevery=10, ms=4, marker='P')
plt.plot(t6['Time in Minutes'],t6['Average-Pb4'], label='T6-Pb4', color='C6', markevery=10, ms=4, marker='x')
plt.plot(sst3['Time in Minutes'],sst3['Average-Pb4'], linestyle='-.', label='SS-T3-Pb4', color='C6', markevery=10, ms=4, marker='X')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('T6vsSS-T3-Avg-Pb.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-HF'], label='T6-Stud3-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(sst3['Time in Minutes'],sst3['Stud2-Mid-HF'], label='SS-T3-Stud3-Top-Fire-HF', color='red', markevery=10, ms=4, marker='v', linestyle='--')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-CF'], label='T6-Stud3-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='s')
plt.plot(sst3['Time in Minutes'],sst3['Stud2-Mid-CF'], label='SS-T3-Stud3-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='d', linestyle='--')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-HF'], label='T6-Stud3-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='x')
plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-CF'], label='T6-Stud3-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='+')
plt.xlabel('Time(min)', fontsize=14)
plt.ylabel('Temperature(°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T6vsSS-T3-Studs.pdf', bbox_inches='tight')
plt.show()
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-HF'], label='T6-Stud3-Top-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Fire-CF'], label='T6-Stud3-Top-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-HF'], label='T6-Stud3-Top-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Top-Amb-CF'], label='T6-Stud3-Top-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Top-HF'], linestyle='--', label='SS-T3-Stud3-Top-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Top-CF'], linestyle='--', label='SS-T3-Stud3-Top-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud3-Top.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud3-Mid-Fire-HF'], label='T6-Stud3-Mid-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Mid-Fire-CF'], label='T6-Stud3-Mid-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Mid-Amb-HF'], label='T6-Stud3-Mid-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Mid-Amb-CF'], label='T6-Stud3-Mid-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Mid-HF'], linestyle='--', label='SS-T3-Stud3-Mid-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Mid-CF'], linestyle='--', label='SS-T3-Stud3-Mid-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud3-Mid.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud3-Bottom-Fire-HF'], label='T6-Stud3-Bottom-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Bottom-Fire-CF'], label='T6-Stud3-Bottom-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Bottom-Amb-HF'], label='T6-Stud3-Bottom-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud3-Bottom-Amb-CF'], label='T6-Stud3-Bottom-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Bottom-HF'], linestyle='--', label='SS-T3-Stud3-Bottom-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Bottom-CF'], linestyle='--', label='SS-T3-Stud3-Bottom-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud3-Bottom.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud4-Top-Fire-HF'], label='T6-Stud4-Top-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Top-Fire-CF'], label='T6-Stud4-Top-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Top-Amb-HF'], label='T6-Stud4-Top-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Top-Amb-CF'], label='T6-Stud4-Top-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Top-HF'], linestyle='--', label='SS-T3-Stud4-Top-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Top-CF'], linestyle='--', label='SS-T3-Stud4-Top-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud4-Top.pdf', bbox_inches='tight')
#plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud4-Mid-Fire-HF'], label='T6-Stud4-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Mid-Fire-CF'], label='T6-Stud4-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Mid-Amb-HF'], label='T6-Stud4-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Mid-Amb-CF'], label='T6-Stud4-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Mid-HF'], linestyle='--', label='SS-T3-Stud4-Mid-HF', color='red', markevery=10, ms=4, marker='>')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Mid-CF'], linestyle='--', label='SS-T3-Stud4-Mid-CF', color='C0', markevery=10, ms=4, marker='+')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud4-Mid.pdf', bbox_inches='tight')
#plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud4-Bottom-Fire-HF'], label='T6-Stud4-Bottom-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Bottom-Fire-CF'], label='T6-Stud4-Bottom-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Bottom-Amb-HF'], label='T6-Stud4-Bottom-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Bottom-Amb-CF'], label='T6-Stud4-Bottom-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Bottom-HF'], linestyle='--', label='SS-T3-Stud4-Bottom-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Bottom-CF'], linestyle='--', label='SS-T3-Stud4-Bottom-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud4-Bottom.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud2-Mid-Fire-HF'], label='T6-Stud2-Mid-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud2-Mid-Fire-CF'], label='T6-Stud2-Mid-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud2-Mid-Amb-HF'], label='T6-Stud2-Mid-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud2-Mid-Amb-CF'], label='T6-Stud2-Mid-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud2-Mid-HF'], linestyle='--', label='SS-T3-Stud2-Mid-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud2-Mid-CF'], linestyle='--', label='SS-T3-Stud2-Mid-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud2-Mid.pdf', bbox_inches='tight')
#plt.show()
#
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud5-Mid-Fire-HF'], label='T6-Stud5-Mid-Fire-HF', color='red')
#plt.plot(t6['Time in Minutes'],t6['Stud5-Mid-Fire-CF'], label='T6-Stud5-Mid-Fire-CF', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud5-Mid-Amb-HF'], label='T6-Stud5-Mid-Amb-HF', color='C1')
#plt.plot(t6['Time in Minutes'],t6['Stud5-Mid-Amb-CF'], label='T6-Stud5-Mid-Amb-CF', color='C2')
#plt.plot(sst3['Time in Minutes'],sst3['Stud5-Mid-HF'], linestyle='--', label='SS-T3-Stud5-Mid-HF', color='red')
#plt.plot(sst3['Time in Minutes'],sst3['Stud5-Mid-CF'], linestyle='--', label='SS-T3-Stud5-Mid-CF', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Temperature(°C)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Stud5-Mid.pdf', bbox_inches='tight')
#plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud3-Axial'], label='T6-Stud3-Axial', color='C0')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Axial'], linestyle='--', label='SS-T3-Stud3-Axial', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Axial'], label='T6-Stud4-Axial', color='C3')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Axial'], linestyle='--', label='SS-T3-Stud4-Axial', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Axial (kN)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Axial.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Stud3-Mid'], label='T6-Stud3-Lateral', color='C0')
#plt.plot(sst3['Time in Minutes'],sst3['Stud3-Mid'], linestyle='--', label='SS-T3-Stud3-Lateral', color='C0')
#plt.plot(t6['Time in Minutes'],t6['Stud4-Mid'], label='T6-Stud4-Lateral', color='C3')
#plt.plot(sst3['Time in Minutes'],sst3['Stud4-Mid'], linestyle='--', label='SS-T3-Stud4-Lateral', color='C3')
#plt.xlabel('Time(min)')
#plt.ylabel('Lateral Deflection(mm)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Lateral.pdf', bbox_inches='tight')
#plt.show()
#
#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(t6['Time in Minutes'],t6['Load in kN'], label='T6-Load', color='C0')
#plt.plot(sst3['Time in Minutes'],sst3['Load in kN'], linestyle='--', label='SS-T3-Load', color='C0')
#plt.xlabel('Time(min)')
#plt.ylabel('Applied Axial Load(kN)')
#plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=4)
#plt.gcf()
#plt.savefig('T6vsSS-T3-Load.pdf', bbox_inches='tight')
#plt.show()