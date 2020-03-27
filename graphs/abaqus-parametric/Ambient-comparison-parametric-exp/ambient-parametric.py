import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
at1 = pd.read_csv('AT1-fe.csv')
at2 = pd.read_csv('AT2-fe.csv')
at3 = pd.read_csv('AT3-fe.csv')
at4 = pd.read_csv('AT4-fe.csv')
at5 = pd.read_csv('AT5-fe.csv')
ds1 = pd.read_csv('DS-70-075-2x16-gen-r0.csv')
sl1 = pd.read_csv('SL-70-075-2x16-gen-r0.csv')
sl2 = pd.read_csv('SL-70-095-2x16-gen-r0.csv')
sl3 = pd.read_csv('SL-90-075-2x16-gen-r0.csv')
sl4 = pd.read_csv('SL-90-095-2x16-gen-r0.csv')
st1 = pd.read_csv('ST-70-075-2x16-gen-r0.csv')
st2 = pd.read_csv('ST-70-095-2x16-gen-r0.csv')
st3 = pd.read_csv('ST-90-075-2x16-gen-r0.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([0,30])
# ax.set_ylim([0,80])
plt.plot(ds1['Displacement in mm'],ds1['Load in kN'], label="DS-70-0.75", color='red', linestyle='-', markevery=20, ms=4, marker='o')
plt.plot(at4['Displacement in mm'],at4['Load in kN'], label="DS-70-0.95 (AT4)", color='red', linestyle='--', markevery=20, ms=4, marker='v')
plt.plot(at2['Displacement in mm'],at2['Load in kN'], label="DS-90-0.75 (AT2)", color='red', linestyle='-.', markevery=20, ms=4, marker='s')
plt.plot(at1['Displacement in mm'],at1['Load in kN'], label="DS-90-0.95 (AT1)", color='red', linestyle=':', markevery=20, ms=4, marker='d')
plt.plot(sl1['Displacement in mm'],sl1['Load in kN'], label="SL-70-0.75", color='C0', linestyle='-', markevery=20, ms=4, marker='x')
plt.plot(sl2['Displacement in mm'],sl2['Load in kN'], label="SL-70-0.95", color='C0', linestyle='--', markevery=20, ms=4, marker='p')
plt.plot(sl3['Displacement in mm'],sl3['Load in kN'], label="SL-90-0.75", color='C0', linestyle='-.', markevery=20, ms=4, marker='h')
plt.plot(sl4['Displacement in mm'],sl4['Load in kN'], label="SL-90-0.95", color='C0', linestyle=':', markevery=20, ms=4, marker='+')
plt.plot(st1['Displacement in mm'],st1['Load in kN'], label="ST-70-0.75", color='C2', linestyle='-', markevery=50, ms=4, marker='*')
plt.plot(st2['Displacement in mm'],st2['Load in kN'], label="ST-70-0.95", color='C2', linestyle='--', markevery=20, ms=4, marker='1')
plt.plot(st3['Displacement in mm'],st3['Load in kN'], label="ST-90-0.75", color='C2', linestyle='-.', markevery=20, ms=4, marker='X')
plt.plot(at5['Displacement in mm'],at5['Load in kN'], label="ST-90-0.95 (AT5)", color='C2', linestyle=':', markevery=20, ms=4, marker='H')
plt.xlabel('Displacement (mm)', fontsize=14)
plt.ylabel('Load (kN)', fontsize=14)
plt.legend(fontsize=14, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.gcf()
plt.savefig('ambient-parametric.pdf', bbox_inches='tight')
plt.show()

