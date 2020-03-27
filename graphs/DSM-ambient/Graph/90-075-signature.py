import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
z = pd.read_csv('90-075-measured-r2.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.set_xlim([0,30])
ax.set_ylim([0,2])
plt.plot(z['Length'],z['Load factor'], label='', color='C0')
plt.plot(70,0.13728, color='red', label="70 mm", marker='o')
plt.plot(300,0.21584, color='C0', label="300 mm", marker='o')
plt.plot(1000,0.40137, color='C1', label="1000 mm", marker='o')
plt.plot(3000,0.053427, color='C2', label="3000 mm", marker='o')
#plt.title('AT1 - Load vs Axial Displacement')
plt.xlabel('Length (mm)', fontsize=16)
plt.ylabel('Load factor', fontsize=16)
plt.xscale('log')
plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('90-075-signature.pdf', bbox_inches='tight')
plt.show()

# ax = plt.axes()        
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# plt.plot(z['Stud2_Top'],z['Load in kN'], label="Stud2-Top", color='red', markevery=25, ms=4, marker='o')
# plt.plot(z['Stud2_Mid'],z['Load in kN'], label="Stud2-Mid", color='C0', markevery=25, ms=4, marker='v')
# plt.plot(z['Stud2_Bottom'],z['Load in kN'], label="Stud2-Bottom", color='C1', markevery=25, ms=4, marker='s')
# plt.plot(z['Stud3_Top'],z['Load in kN'], label="Stud3-Top", color='C2', markevery=25, ms=4, marker='d')
# plt.plot(z['Stud3_Mid'],z['Load in kN'], label="Stud3-Mid", color='C4', markevery=25, ms=4, marker='x')
# plt.plot(z['Stud3_Bottom'],z['Load in kN'], label="Stud3-Bottom", color='C6', markevery=25, ms=4, marker='p')
# #plt.title('AT1 - Load vs Lateral Deflection')
# plt.xlabel('Displacement(mm)')
# plt.ylabel('Load(kN)')
# plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('AT1-Load-Lateral.pdf', bbox_inches='tight')
# plt.show()
