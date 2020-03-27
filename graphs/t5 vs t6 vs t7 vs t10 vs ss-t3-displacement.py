import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
t5 = pd.read_csv('T5.csv')
t6 = pd.read_csv('T6.csv')
t7 = pd.read_csv('T7.csv')
t10 = pd.read_csv('T10.csv')
sst3 = pd.read_csv('SS-T3.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t5['Time in Minutes'],t5['Stud3-Axial'], label='T5-Stud3-Axial', color='red', markevery=10, ms=4, marker='o')
plt.plot(t6['Time in Minutes'],t6['Stud3-Axial'], label='T6-Stud3-Axial', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t7['Time in Minutes'],t7['Stud3-Axial'], label='T7-Stud3-Axial', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t10['Time in Minutes'],t10['Stud3-Axial'], label='T10-Stud3-Axial', color='C2', markevery=500, ms=4, marker='d')
plt.plot(sst3['Time in Minutes'],sst3['Stud3-Axial'], label='SS-T3-Stud3-Axial', color='C4', markevery=10, ms=4, marker='p')
plt.xlabel('Time(min)')
plt.ylabel('Axial Displacement(mm)')
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T5vsT6vsT7vsT10vsSS-T3-Axial.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
plt.plot(t5['Time in Minutes'],t5['Stud3-Mid'], label='T5-Stud3-Lateral', color='red', markevery=10, ms=4, marker='o')
plt.plot(t6['Time in Minutes'],t6['Stud3-Mid'], label='T6-Stud3-Lateral', color='C0', markevery=10, ms=4, marker='v')
plt.plot(t7['Time in Minutes'],t7['Stud3-Mid'], label='T7-Stud3-Lateral', color='C1', markevery=10, ms=4, marker='s')
plt.plot(t10['Time in Minutes'],t10['Stud3-Mid'], label='T10-Stud3-Lateral', color='C2', markevery=500, ms=4, marker='d')
plt.plot(sst3['Time in Minutes'],sst3['Stud3-Mid'], label='SS-T3-Stud3-Lateral', color='C4', markevery=10, ms=4, marker='d')
plt.xlabel('Time(min)')
plt.ylabel('Lateral Deflection(mm)')
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T5vsT6vsT7vsT10vsSS-T3-Lateral.pdf', bbox_inches='tight')
plt.show()

