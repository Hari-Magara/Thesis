import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "times new roman"
plt.rcParams['lines.linewidth'] = 1.25
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
   
z = pd.read_csv('frl-parametric.csv')

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([50,200])
ax.set_ylim([0,1])
plt.scatter(z['DS-70-075-2x16'],z['LR'], label="DS-70-0.75", color='red', marker='o', s=50)
plt.scatter(z['DS-70-075-2x16-AI'],z['LR'], label="DS-70-0.75-AI", color='C0', marker='v', s=50)
plt.scatter(z['DS-70-075-2x16-BI'],z['LR'], label="DS-70-0.75-BI", color='C1', marker='s', s=50)
plt.scatter(z['DS-70-095-2x16-AI'],z['LR'], label="DS-70-0.95-AI", color='C2', marker='d', s=50)
plt.scatter(z['DS-70-095-2x16-BI'],z['LR'], label="DS-70-0.95-BI", color='C4', marker='x', s=50)
plt.scatter(z['DS-90-075-2x16-AI'],z['LR'], label="DS-90-0.75-AI", color='C6', marker='p', s=50)
plt.scatter(z['DS-90-075-2x16-BI'],z['LR'], label="DS-90-0.95-BI", color='C7', marker='h', s=50)
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Load Ratio - LR', fontsize=16)
plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('frl-DS-parametric.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([30,175])
ax.set_ylim([0,1])
plt.scatter(z['SL-70-075-2x16'],z['LR'], label="SL-70-0.75", color='red', marker='o', s=50)
plt.scatter(z['SL-70-075-2x16-FI'],z['LR'], label="SL-70-0.75-FI", color='C0', marker='v', s=50)
plt.scatter(z['SL-70-095-2x16'],z['LR'], label="SL-70-0.95", color='C1', marker='s', s=50)
plt.scatter(z['SL-70-095-2x16-FI'],z['LR'], label="SL-70-0.95-FI", color='C2', marker='d', s=50)
plt.scatter(z['SL-90-075-2x16-FI'],z['LR'], label="SL-90-0.75-FI", color='C4', marker='x', s=50)
plt.scatter(z['SL-90-095-2x16'],z['LR'], label="SL-90-0.95", color='C6', marker='p', s=50)
plt.scatter(z['SL-90-095-2x16-FI'],z['LR'], label="SL-90-0.95-FI", color='C7', marker='h', s=50)
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Load Ratio - LR', fontsize=16)
plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('frl-SL-parametric.pdf', bbox_inches='tight')
plt.show()

ax = plt.axes()        
ax.yaxis.grid(True, linestyle=':') # horizontal lines
ax.xaxis.grid(True, linestyle=':') # vertical lines
ax.set_xlim([50,200])
ax.set_ylim([0,1])
plt.scatter(z['ST-70-075-2x16'],z['LR'], label="ST-70-0.75", color='red', marker='o', s=50)
plt.scatter(z['ST-70-075-2x16-FI'],z['LR'], label="ST-70-0.75-FI", color='C0', marker='v', s=50)
plt.scatter(z['ST-70-095-2x16'],z['LR'], label="ST-70-0.95", color='C1', marker='s', s=50)
plt.scatter(z['ST-70-095-2x16-FI'],z['LR'], label="ST-70-0.95-FI", color='C2', marker='d', s=50)
plt.scatter(z['ST-90-075-2x16-FI'],z['LR'], label="ST-90-0.75-FI", color='C4', marker='x', s=50)
plt.scatter(z['ST-90-095-2x16'],z['LR'], label="ST-90-0.95", color='C6', marker='p', s=50)
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Load Ratio - LR', fontsize=16)
plt.legend(fontsize=16, loc=9, bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.gcf()
plt.savefig('frl-ST-parametric.pdf', bbox_inches='tight')
plt.show()

