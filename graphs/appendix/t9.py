import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
s = pd.read_csv('standard fire curve.csv')
t9 = pd.read_csv('t9-experiment.csv')

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Furnace-Top-Left'], label='T9-Furnace-Top-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Furnace-Top-Right'], label='T9-Furnace-Top-Right', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Furnace-Bottom-Left'], label='T9-Furnace-Bottom-Left', color='C2', markevery=10, ms=4, marker='d')
plt.plot(t9['Time in Minutes'],t9['Furnace-Bottom-Right'], label='T9-Furnace-Bottom-Right', color='C4', markevery=10, ms=4, marker='>')
#plt.title('T9-Furnace')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Furnace-ap.pdf', bbox_inches='tight')
plt.show()

# ax = plt.axes()     
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.xaxis.label.set_size(12)
# ax.yaxis.label.set_size(12)
# ax.set_xlim([0,200])
# plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
# plt.plot(t9['Time in Minutes'],t9['Average-Furnace'], label='T9-Furnace', color='maroon')
# plt.plot(t9['Time in Minutes'],t9['Average-Pb1'], label='T9-Pb1', color='red', markevery=10, ms=4, marker='o')
# plt.plot(t9['Time in Minutes'],t9['Average-Pb1-Pb2'], label='T9-Pb1-Pb2', color='C0', markevery=10, ms=4, marker='v')
# plt.plot(t9['Time in Minutes'],t9['Average-Pb2'], label='T9-Pb2', color='C1', markevery=10, ms=4, marker='s')
# plt.plot(t9['Time in Minutes'],t9['Average-Pb3'], label='T9-Pb3', color='C2', markevery=10, ms=4, marker='d')
# plt.plot(t9['Time in Minutes'],t9['Average-Pb3-Pb4'], label='T9-Pb3-Pb4', color='C4', markevery=10, ms=4, marker='>')
# plt.plot(t9['Time in Minutes'],t9['Average-Pb4'], label='T9-Pb4', color='C6', markevery=10, ms=4, marker='+')
# #plt.title('T9-Average Plasterboard')
# plt.xlabel('Time (min)', fontsize=14)
# plt.ylabel('Temperature (°C)', fontsize=14)
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('T9-Average-Pb-ap.pdf', bbox_inches='tight')
# plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Pb1-Top-Left'], label='T9-Pb1-Top-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Pb1-Top-Right'], label='T9-Pb1-Top-Right', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Pb1-Mid-Mid'], label='T9-Pb1-Mid-Mid', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Pb1-Bottom-Left'], label='T9-Pb1-Bottom-Left', color='C2', markevery=10, ms=4, marker='d')
plt.plot(t9['Time in Minutes'],t9['Pb1-Bottom-Right'], label='T9-Pb1-Bottom-Right', color='C4', markevery=10, ms=4, marker='>')
#plt.title('T9-Pb1')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Pb1-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
#plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Pb1-Pb2-Mid-Left'], label='T9-Pb1-Pb2-Mid-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Pb1-Pb2-Mid-Mid'], label='T9-Pb1-Pb2-Mid-Mid', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Pb1-Pb2-Mid-Right'], label='T9-Pb1-Pb2-Mid-Right', color='C1', markevery=10, ms=4, marker='s')
#plt.title('T9-Pb1-Pb2')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Pb1-Pb2-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
#plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Pb2-Mid-Left'], label='T9-Pb2-Mid-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Pb2-Mid-Mid'], label='T9-Pb2-Mid-Mid', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Pb2-Mid-Right'], label='T9-Pb2-Mid-Right', color='C1', markevery=10, ms=4, marker='s')
#plt.title('T9-Pb2')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Pb2-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
#plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Pb3-Mid-Left'], label='T9-Pb3-Mid-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Pb3-Mid-Mid'], label='T9-Pb3-Mid-Mid', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Pb3-Mid-Right'], label='T9-Pb3-Mid-Right', color='C1', markevery=10, ms=4, marker='s')
#plt.title('T9-Pb3')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Pb3-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
#plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Pb3-Pb4-Mid-Left'], label='T9-Pb3-Pb4-Mid-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Pb3-Pb4-Mid-Mid'], label='T9-Pb3-Pb4-Mid-Mid', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Pb3-Pb4-Mid-Right'], label='T9-Pb3-Pb4-Mid-Right', color='C1', markevery=10, ms=4, marker='s')
#plt.title('T9-Pb3-Pb4')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Pb3-Pb4-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.set_xlim([0,200])
#plt.plot(s['ISO 834-Time'],s['ISO 834-Temp'], linestyle='--', label='Standard fire curve', color='maroon')
plt.plot(t9['Time in Minutes'],t9['Pb4-Top-Left'], label='T9-Pb4-Top-Left', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Pb4-Top-Right'], label='T9-Pb4-Top-Right', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Pb4-Mid-Mid'], label='T9-Pb4-Mid-Mid', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Pb4-Bottom-Left'], label='T9-Pb4-Bottom-Left', color='C2', markevery=10, ms=4, marker='d')
plt.plot(t9['Time in Minutes'],t9['Pb4-Bottom-Right'], label='T9-Pb4-Bottom-Right', color='C4', markevery=10, ms=4, marker='>')
plt.plot(t9['Time in Minutes'],t9['Pb4-Top of stud'], label='T9-Pb4-Top of stud', color='C5', markevery=10, ms=4, marker='+')
plt.plot(t9['Time in Minutes'],t9['Pb4-Inbetween stud'], label='T9-Pb4-Inbetween stud', color='C6', markevery=10, ms=4, marker='<')
#plt.title('T9-Pb4')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Pb4-ap.pdf', bbox_inches='tight')
plt.show()

# ax = plt.axes()        
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.xaxis.label.set_size(12)
# ax.yaxis.label.set_size(12)
# plt.plot(t9['Time in Minutes'],t9['Stud2-Top-Amb-HF'], label='T9-Stud2-Top-Amb-HF', color='red', markevery=10, ms=4, marker='o')
# plt.plot(t9['Time in Minutes'],t9['Stud2-Top-Amb-CF'], label='T9-Stud2-Top-Amb-CF', color='C0', markevery=10, ms=4, marker='v')
# #plt.title('T9-Stud2-Top-Amb')
# plt.xlabel('Time (min)', fontsize=14)
# plt.ylabel('Temperature (°C)', fontsize=14)
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('T9-Stud2-Top-Amb-ap.pdf', bbox_inches='tight')
# plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud2-Mid-Fire-HF'], label='T9-Stud2-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud2-Mid-Fire-CF'], label='T9-Stud2-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud2-Mid-Amb-HF'], label='T9-Stud2-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud2-Mid-Amb-CF'], label='T9-Stud2-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud2-Mid')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud2-Mid-ap.pdf', bbox_inches='tight')
plt.show()

# ax = plt.axes()        
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.xaxis.label.set_size(12)
# ax.yaxis.label.set_size(12)
# plt.plot(t9['Time in Minutes'],t9['Stud2-Bottom-Amb-HF'], label='T9-Stud2-Bottom-Amb-HF', color='red', markevery=10, ms=4, marker='o')
# plt.plot(t9['Time in Minutes'],t9['Stud2-Bottom-Amb-CF'], label='T9-Stud2-Bottom-Amb-CF', color='C0', markevery=10, ms=4, marker='v')
# #plt.title('T9-Stud2-Bottom-Amb')
# plt.xlabel('Time (min)', fontsize=14)
# plt.ylabel('Temperature (°C)', fontsize=14)
# plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('T9-Stud2-Bottom-Amb-ap.pdf', bbox_inches='tight')
# plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud3-Top-Fire-HF'], label='T9-Stud3-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud3-Top-Fire-CF'], label='T9-Stud3-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud3-Top-Amb-HF'], label='T9-Stud3-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud3-Top-Amb-CF'], label='T9-Stud3-Top-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud3-Top')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud3-Top-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud3-Mid-Fire-HF'], label='T9-Stud3-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud3-Mid-Fire-CF'], label='T9-Stud3-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud3-Mid-Amb-HF'], label='T9-Stud3-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud3-Mid-Amb-CF'], label='T9-Stud3-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud3-Mid')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud3-Mid-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud3-Bottom-Fire-HF'], label='T9-Stud3-Bottom-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud3-Bottom-Fire-CF'], label='T9-Stud3-Bottom-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud3-Bottom-Amb-HF'], label='T9-Stud3-Bottom-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud3-Bottom-Amb-CF'], label='T9-Stud3-Bottom-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud3-Bottom')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud3-Bottom-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud4-Top-Fire-HF'], label='T9-Stud4-Top-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud4-Top-Fire-CF'], label='T9-Stud4-Top-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud4-Top-Amb-HF'], label='T9-Stud4-Top-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud4-Top-Amb-CF'], label='T9-Stud4-Top-Amb-CF', color='C1', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud4-Top')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud4-Top-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Fire-HF'], label='T9-Stud4-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Fire-CF'], label='T9-Stud4-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Amb-HF'], label='T9-Stud4-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid-Amb-CF'], label='T9-Stud4-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud4-Mid')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud4-Mid-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud4-Bottom-Fire-HF'], label='T9-Stud4-Bottom-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud4-Bottom-Fire-CF'], label='T9-Stud4-Bottom-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
# plt.plot(t9['Time in Minutes'],t9['Stud4-Bottom-Amb-HF'], label='T9-Stud4-Bottom-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
# plt.plot(t9['Time in Minutes'],t9['Stud4-Bottom-Amb-CF'], label='T9-Stud4-Bottom-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud4-Bottom')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud4-Bottom-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud5-Mid-Fire-HF'], label='T9-Stud5-Mid-Fire-HF', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud5-Mid-Fire-CF'], label='T9-Stud5-Mid-Fire-CF', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud5-Mid-Amb-HF'], label='T9-Stud5-Mid-Amb-HF', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud5-Mid-Amb-CF'], label='T9-Stud5-Mid-Amb-CF', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Stud5-Mid')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Stud5-Mid-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud2-Axial'], label='T9-Stud3-Axial', color='red', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud3-Axial'], label='T9-Stud3-Axial', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud4-Axial'], label='T9-Stud4-Axial', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t9['Time in Minutes'],t9['Stud5-Axial'], label='T9-Stud3-Axial', color='C2', markevery=10, ms=4, marker='d')
#plt.title('T9-Time vs Axial Displacement')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Axial Displacement (mm)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Axial-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t9['Time in Minutes'],t9['Stud3-Top'], label='T9-Stud3-Top', color='C0', markevery=10, ms=4, marker='o')
plt.plot(t9['Time in Minutes'],t9['Stud3-Mid'], label='T9-Stud3-Mid', color='C1', markevery=10, ms=4, marker='v')
plt.plot(t9['Time in Minutes'],t9['Stud3-Bottom'], label='T9-Stud3-Bottom', color='C2', markevery=10, ms=4, marker='s')
# plt.plot(t9['Time in Minutes'],t9['Stud4-Top'], label='T9-Stud4-Top', color='C4', markevery=10, ms=4, marker='x')
plt.plot(t9['Time in Minutes'],t9['Stud4-Mid'], label='T9-Stud4-Mid', color='C6', markevery=10, ms=4, marker='p')
# plt.plot(t9['Time in Minutes'],t9['Stud4-Bottom'], label='T9-Stud4-Bottom', color='C7', markevery=10, ms=4, marker='')
#plt.title('T9-Time vs Lateral Displacement')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Lateral Deflection (mm)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Lateral-ap.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_ylim([0,38])
plt.plot(t9['Time in Minutes'],t9['Load in kN'], label='T9-Load', color='C0', markevery=10, ms=4, marker='o')
#plt.title('T9-Time vs Applied Axial Load')
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Applied Axial Load (kN)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T9-Load-ap.pdf', bbox_inches='tight')
plt.show()