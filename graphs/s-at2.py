import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
z = pd.read_csv('s-at2.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.set_xlim([0,10])
#ax.set_ylim([0,60])
plt.plot(z['Stud1-Axial'],z['Stud1-Load'], label="Stud1-Axial", color='red', markevery=20, ms=4, marker='o')
plt.plot(z['Stud2-Axial'],z['Stud2-Load'], label="Stud2-Axial", color='C0', markevery=20, ms=4, marker='v')
plt.plot(z['Stud3-Axial'],z['Stud3-Load'], label="Stud3-Axial", color='C1', markevery=20, ms=4, marker='s')
plt.plot(z['Stud4-Axial'],z['Stud4-Load'], label="Stud4-Axial", color='C2', markevery=20, ms=4, marker='d')
#plt.title('AT1 - Load vs Axial Displacement')
plt.xlabel('Displacement(mm)')
plt.ylabel('Load(kN)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('S-AT2-Load-Axial.pdf', bbox_inches='tight')
plt.show(0)

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#plt.plot(z['Stud1_Top'],z['Load in kN'], label="Stud1-Top", color='red', markevery=20, ms=4, marker='o')
#plt.plot(z['Stud1_Mid'],z['Load in kN'], label="Stud1-Mid", color='C0', markevery=20, ms=4, marker='v')
#plt.plot(z['Stud1_Bottom'],z['Load in kN'], label="Stud1-Bottom", color='C1', markevery=20, ms=4, marker='s')
#plt.plot(z['Stud2_Top'],z['Load in kN'], label="Stud2-Top", color='C2', markevery=20, ms=4, marker='d')
#plt.plot(z['Stud2_Mid'],z['Load in kN'], label="Stud2-Mid", color='C4', markevery=20, ms=4, marker='x')
#plt.plot(z['Stud2_Bottom'],z['Load in kN'], label="Stud2-Bottom", color='C6', markevery=20, ms=4, marker='p')
##plt.title('AT1 - Load vs Lateral Deflection')
#plt.xlabel('Displacement(mm)')
#plt.ylabel('Load(kN)')
#plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('S-AT2-Load-Lateral.pdf', bbox_inches='tight')
#plt.show()
