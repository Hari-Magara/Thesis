import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
t1 = pd.read_csv('T1.csv')
t2 = pd.read_csv('T2.csv')
t4 = pd.read_csv('T4.csv')
sst1 = pd.read_csv('SS-T1.csv')
sst2 = pd.read_csv('SS-T2.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t1['Time in Minutes'],t1['Stud3-Axial'], label='T1-Stud3-Axial', color='red', markevery=10, ms=4, marker='o')
plt.plot(t2['Time in Minutes'],t2['Stud3-Axial'], label='T2-Stud3-Axial', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t4['Time in Minutes'],t4['Stud3-Axial'], label='T4-Stud3-Axial', color='C1', markevery=10, ms=4, marker='s')
plt.plot(sst1['Time in Minutes'],sst1['Stud3-Axial'], label='SS-T1-Stud3-Axial', color='C2', markevery=10, ms=4, marker='d')
plt.plot(sst2['Time in Minutes'],sst2['Stud3-Axial'], label='SS-T2-Stud3-Axial', color='C4', markevery=10, ms=4, marker='p')
plt.xlabel('Time(min)')
plt.ylabel('Axial Displacement(mm)')
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1vsT2vsT4vsSS-T1vsSS-T2-Axial.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t1['Time in Minutes'],t1['Stud3-Mid'], label='T1-Stud3-Lateral', color='red', markevery=10, ms=4, marker='o')
plt.plot(t2['Time in Minutes'],t2['Stud3-Mid'], label='T2-Stud3-Lateral', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t4['Time in Minutes'],t4['Stud3-Mid'], label='T4-Stud3-Lateral', color='C1', markevery=10, ms=4, marker='s')
plt.plot(sst1['Time in Minutes'],sst1['Stud3-Mid'], label='SS-T1-Stud3-Lateral', color='C2', markevery=10, ms=4, marker='d')
plt.plot(sst2['Time in Minutes'],sst2['Stud3-Mid'], label='SS-T2-Stud3-Lateral', color='C4', markevery=10, ms=4, marker='p')
plt.xlabel('Time(min)')
plt.ylabel('Lateral Deflection(mm)')
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T1vsT2vsT4vsSS-T1vsSS-T2-Lateral.pdf', bbox_inches='tight')
plt.show()

