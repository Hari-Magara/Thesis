import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
z = pd.read_csv('at1.csv')

#ax = plt.axes()     
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(z['Time in Sec'],z['Stud1_Axial'], label="Stud1_Axial")
#plt.plot(z['Time in Sec'],z['Stud2_Axial'], label="Stud2_Axial")
#plt.plot(z['Time in Sec'],z['Stud3_Axial'], label="Stud3_Axial")
#plt.plot(z['Time in Sec'],z['Stud4_Axial'], label="Stud4_Axial")
#plt.title('Time vs Axial Displacement')
#plt.xlabel('Time(sec)')
#plt.ylabel('Axial Displacement(mm)')
#plt.legend(loc='best')
#plt.gcf()
#plt.savefig('Time vs Axial.pdf')
#plt.show()
#
#
#ax = plt.axes()     
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(z['Time in Sec'],z['Stud3_Top'], label="Stud3_Top")
#plt.plot(z['Time in Sec'],z['Stud3_Mid'], label="Stud3_Mid")
#plt.plot(z['Time in Sec'],z['Stud3_Bottom'], label="Stud3_Bottom")
#plt.title('Time vs Lateral Deflection')
#plt.xlabel('Displacement(mm)')
#plt.ylabel('Time(sec)')
#plt.legend(loc='best')
#plt.gcf()
#plt.savefig('Stud3-Time vs Lateral.pdf')
#plt.show()
#
#ax = plt.axes()     
#ax.yaxis.grid(True, linestyle=':') # horizontal lines
#ax.xaxis.grid(True, linestyle=':') # vertical lines
#ax.xaxis.label.set_size(12)
#ax.yaxis.label.set_size(12)
#plt.plot(z['Time in Sec'],z['Stud2_Top'], label="Stud2_Top")
#plt.plot(z['Time in Sec'],z['Stud2_Mid'], label="Stud2_Mid")
#plt.plot(z['Time in Sec'],z['Stud2_Bottom'], label="Stud2_Bottom")
#plt.title('Time vs Lateral Deflection')
#plt.xlabel('Displacement(mm)')
#plt.ylabel('Time(sec)')
#plt.legend(loc='best')
#plt.gcf()
#plt.savefig('Stud2-Time vs Lateral.pdf')
#plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,30])
ax.set_ylim([0,80])
plt.plot(z['Stud1_Axial'],z['Load in kN'], label="Stud1-Axial", color='red', markevery=25, ms=4, marker='o')
plt.plot(z['Stud2_Axial'],z['Load in kN'], label="Stud2-Axial", color='C0', markevery=25, ms=4, marker='v')
plt.plot(z['Stud3_Axial'],z['Load in kN'], label="Stud3-Axial", color='C1', markevery=25, ms=4, marker='s')
plt.plot(z['Stud4_Axial'],z['Load in kN'], label="Stud4-Axial", color='C2', markevery=25, ms=4, marker='d')
#plt.title('AT1 - Load vs Axial Displacement')
plt.xlabel('Displacement(mm)')
plt.ylabel('Load(kN)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('AT1-Load-Axial.pdf', bbox_inches='tight')
plt.show(0)

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
plt.plot(z['Stud2_Top'],z['Load in kN'], label="Stud2-Top", color='red', markevery=25, ms=4, marker='o')
plt.plot(z['Stud2_Mid'],z['Load in kN'], label="Stud2-Mid", color='C0', markevery=25, ms=4, marker='v')
plt.plot(z['Stud2_Bottom'],z['Load in kN'], label="Stud2-Bottom", color='C1', markevery=25, ms=4, marker='s')
plt.plot(z['Stud3_Top'],z['Load in kN'], label="Stud3-Top", color='C2', markevery=25, ms=4, marker='d')
plt.plot(z['Stud3_Mid'],z['Load in kN'], label="Stud3-Mid", color='C4', markevery=25, ms=4, marker='x')
plt.plot(z['Stud3_Bottom'],z['Load in kN'], label="Stud3-Bottom", color='C6', markevery=25, ms=4, marker='p')
#plt.title('AT1 - Load vs Lateral Deflection')
plt.xlabel('Deflection(mm)')
plt.ylabel('Load(kN)')
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('AT1-Load-Lateral.pdf', bbox_inches='tight')
plt.show()
