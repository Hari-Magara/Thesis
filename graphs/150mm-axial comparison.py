import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
at5 = pd.read_csv('at5-r1.csv')
sat3 = pd.read_csv('s-at3-r0.csv')


ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horiat5ontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,25])
ax.set_ylim([0,70])
plt.plot(at5['Stud2_Axial'],at5['Load in kN'], label="AT5-Stud2-Axial", color='red', markevery=25, ms=4, marker='o')
plt.plot(sat3['Stud2_Axial'],sat3['Load in kN'], label="S-AT3-Stud3-Axial", color='C0', markevery=25, ms=4, marker='v')
#plt.title('AT1 - Load vs Axial Displacement')
plt.xlabel('Displacement(mm)', fontsize=14)
plt.ylabel('Load(kN)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('150mm-Axial-comparison.pdf', bbox_inches='tight')
plt.show()

#ax = plt.axes()        
#ax.yaxis.grid(True, linestyle=':') # horiat5ontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#plt.plot(at5['Stud2_Top'],at5['Load in kN'], label="Stud2-Top", color='red', markevery=25, ms=4, marker='o')
#plt.plot(at5['Stud2_Mid'],at5['Load in kN'], label="Stud2-Mid", color='C0', markevery=25, ms=4, marker='v')
#plt.plot(at5['Stud2_Bottom'],at5['Load in kN'], label="Stud2-Bottom", color='C1', markevery=25, ms=4, marker='s')
#plt.plot(at5['Stud3_Top'],at5['Load in kN'], label="Stud3-Top", color='C2', markevery=25, ms=4, marker='d')
#plt.plot(at5['Stud3_Mid'],at5['Load in kN'], label="Stud3-Mid", color='C4', markevery=25, ms=4, marker='x')
#plt.plot(at5['Stud3_Bottom'],at5['Load in kN'], label="Stud3-Bottom", color='C6', markevery=25, ms=4, marker='p')
##plt.title('AT1 - Load vs Lateral Deflection')
#plt.xlabel('Displacement(mm)')
#plt.ylabel('Load(kN)')
#plt.legend(fontsiat5e=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
#plt.gcf()
#plt.savefig('AT1-Load-Lateral.pdf', bbox_inches='tight')
#plt.show()
