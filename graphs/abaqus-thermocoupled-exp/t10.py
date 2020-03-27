import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
  
z = pd.read_csv('t10-experiment.csv')

#df = pd.read_csv('t10-l_devc.csv',header=1)
#df.insert(1, 'Time in Minutes',df['Time']/60)
#df.to_csv('t10-l_devc.csv', sep=',')

a = pd.read_csv('t10-axial-fe.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud3-Axial'], label='Exp-T10-Stud3-Axial', color='red', markevery=1000, ms=4, marker='o')
plt.plot(a['Time in Minutes'],a['Displacement in mm'], label='FE-T10-Axial', color='C0', markevery=30, ms=4, marker='v')
#plt.title('Test10-Exp vs Fds Pb-l')
plt.xlabel('Time(min)')
plt.ylabel('Axial Displacement(mm)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T10-axial-FE-vs-Exp.pdf', bbox_inches='tight')
plt.show()

l = pd.read_csv('t10-lateral-fe.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Stud3-Mid'], label='Exp-T10-Stud3-Mid', color='red', markevery=1000, ms=4, marker='o')
plt.plot(l['Time in Minutes'],l['Displacement in mm-Stud1'], label='FE-T10-Lateral-Stud1', color='C0', markevery=30, ms=4, marker='v')
# plt.plot(l['Time in Minutes'],l['Displacement in mm-Stud2'], label='FE-T10-Lateral-Stud2', color='C1', markevery=30, ms=4, marker='s')
#plt.title('Test10-Exp vs Fds Pb-l')
plt.xlabel('Time(min)')
plt.ylabel('Lateral Deflection(mm)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T10-lateral-FE-vs-Exp.pdf', bbox_inches='tight')
plt.show()

a = pd.read_csv('t10-axial-fe.csv')
ax = plt.axes()     
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
# ax.set_xlim([0,240])
plt.plot(z['Time in Minutes'],z['Load in kN'], label='Exp-T10-Load', color='red', markevery=1000, ms=4, marker='o')
plt.plot(a['Time in Minutes'],a['Load in kN'], label='FE-T10-Load', color='C0', markevery=30, ms=4, marker='v')
#plt.title('Test10-Exp vs Fds Pb-l')
plt.xlabel('Time(min)')
plt.ylabel('Applied Axial Load(kN)')
plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('T10-load-FE-vs-Exp.pdf', bbox_inches='tight')
plt.show()

# a = pd.read_csv('t10-axial-fe.csv')
# ax = plt.axes()     
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.xaxis.label.set_size(12)
# ax.yaxis.label.set_size(12)
# # ax.set_xlim([0,240])
# plt.plot(z['Stud3-Axial'],z['Load in kN'], label='Exp-T10-Stud3-Axial', color='red', markevery=30, ms=4, marker='o')
# plt.plot(a['Displacement in mm'],a['Load in kN'], label='FE-T10-Axial', color='C0', markevery=30, ms=4, marker='v')
# #plt.title('Test10-Exp vs Fds Pb-l')
# plt.xlabel('Axial Displacement(mm)')
# plt.ylabel('Applied Axial Load(kN)')
# plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('T10-axial-load-FE-vs-Exp.pdf', bbox_inches='tight')
# plt.show()

# l = pd.read_csv('t10-lateral-fe.csv')
# ax = plt.axes()     
# ax.yaxis.grid(True, linestyle=':') # horizontal lines
# ax.xaxis.grid(True, linestyle=':') # vertical lines
# ax.xaxis.label.set_size(12)
# ax.yaxis.label.set_size(12)
# # ax.set_xlim([0,240])
# plt.plot(z['Stud3-Mid'],z['Load in kN'], label='Exp-T10-Stud3-Mid', color='red', markevery=30, ms=4, marker='o')
# plt.plot(l['Displacement in mm'],l['Load in kN'], label='FE-T10-Lateral', color='C0', markevery=30, ms=4, marker='v')
# #plt.title('Test10-Exp vs Fds Pb-l')
# plt.xlabel('Lateral Deflection(mm)')
# plt.ylabel('Applied Axial Load(kN)')
# plt.legend(fontsize=12, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
# plt.gcf()
# plt.savefig('T10-lateral-load-FE-vs-Exp.pdf', bbox_inches='tight')
# plt.show()

