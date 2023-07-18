import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
pdms_teng = pd.read_excel('/home/yxt/impact_data/6_21/good/section/new/pdms_tengs.xlsx')
pdms_data0 = pdms_teng['PDMS']
pdms_time0 = pdms_teng['time']
pdms_data = np.array(pdms_data0)
pdms_time = np.array(pdms_time0)

    
df_sonar = pd.read_excel('/home/yxt/impact_data/6_21/good/section/new/sonar.xlsx')
sonar_data0 = df_sonar['sonar']
sonar_time0 = df_sonar['time']
sonar_data = np.array(sonar_data0)
sonar_time = np.array(sonar_time0)

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('TENG (V)', color=color)
ax1.plot(pdms_time, pdms_data, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Distance (cm)', color=color)  # we already handled the x-label with ax1
ax2.plot(sonar_time, sonar_data, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


