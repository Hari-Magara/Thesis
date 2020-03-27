import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
z = pd.read_csv('AT5-r1.csv')
f = pd.read_csv('AT5-fe.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,30])
ax.set_ylim([0,80])
plt.plot(z['Stud1_Axial'],z['Load in kN'], label="Stud2-Axial", color='red', markevery=25, ms=4, marker='o')
plt.plot(z['Stud2_Axial'],z['Load in kN'], label="Stud3-Axial", color='C0', markevery=25, ms=4, marker='v')
plt.plot(z['Stud3_Axial'],z['Load in kN'], label="Stud4-Axial", color='C1', markevery=25, ms=4, marker='s')
plt.plot(z['Stud4_Axial'],z['Load in kN'], label="Stud5-Axial", color='C2', markevery=25, ms=4, marker='d')
plt.plot(f['Displacement in mm'],f['Load in kN'], label="FEA", color='C4', markevery=25, ms=4, marker='*')
#plt.title('AT4 - Load vs Axial Displacement')
plt.xlabel('Displacement (mm)', fontsize=16)
plt.ylabel('Load (kN)', fontsize=16)
plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('AT5-Load-Axial-Exp-vs-FE.pdf', bbox_inches='tight')
plt.show()

# ax = plt.axes()        
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# #ax.set_xlim([-15,30])
# #ax.set_ylim([0,50])
# plt.plot(z['Stud2_Top'],z['Load in kN'], label="Stud3-Top", color='red', markevery=25, ms=4, marker='o')
# plt.plot(z['Stud2_Mid'],z['Load in kN'], label="Stud3-Mid", color='C0', markevery=25, ms=4, marker='v')
# plt.plot(z['Stud2_Bottom'],z['Load in kN'], label="Stud3-Bottom", color='C1', markevery=25, ms=4, marker='s')
# plt.plot(z['Stud3_Top'],z['Load in kN'], label="Stud4-Top", color='C2', markevery=25, ms=4, marker='d')
# plt.plot(z['Stud3_Mid'],z['Load in kN'], label="Stud4-Mid", color='C4', markevery=25, ms=4, marker='x')
# plt.plot(z['Stud3_Bottom'],z['Load in kN'], label="Stud4-Bottom", color='C6', markevery=25, ms=4, marker='p')
# #plt.title('AT4 - Load vs Lateral Deflection')
# plt.xlabel('Displacement (mm)')
# plt.ylabel('Load (kN)')
# plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('AT5-Load-Lateral.pdf', bbox_inches='tight')
# plt.show()
