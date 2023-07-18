import rosbag, rospy
import pandas as pd 
from std_msgs.msg import Float32, UInt8, Float32MultiArray
from teng_arduino.msg import channels
import math

# bag = rosbag.Bag('/home/yxt/impact_data/6_21/good/bag_21.06_15.24_approach_impact1-230s.bag')
bag = rosbag.Bag('/home/yxt/impact_data/6_21/good/section/1.bag')
# bag = rosbag.Bag('/home/yxt/impact_data/6_21/good/section2/1.bag')
sav = "/home/yxt/impact_data/6_21/good/" + 'section/new/'
print(bag)
impact_data = []
impact_time = []

teng_data1 = []
teng_time1 = []

teng_data2 = []
teng_time2 = []

torque_data = []
torque_time = []

sonar_data = []
sonar_time = []

t0 = 1689688958

for topic, msg, t in bag.read_messages(topics=['/impact']):
    impact_data.append(msg.data)
    time = round(t.secs+t.nsecs*1e-9 - t0, 2)
    impact_time.append(time)

    
for topic, msg, t in bag.read_messages(topics=['/TENG_SIGNALS']):
    teng_data1.append(msg.c[0])
    teng_data2.append(msg.c[1])
    time = round(t.secs+t.nsecs*1e-9 - t0, 2)
    teng_time1.append(time)
    
for topic, msg, t in bag.read_messages(topics=['/ee_efforts']):
    torque_data.append(msg.data[1])
    time = round(t.secs+t.nsecs*1e-9 - t0, 2)
    torque_time.append(time)

for topic, msg, t in bag.read_messages(topics=['/Sonar']):
    sonar_data.append(msg.data) 
    time = round(t.secs+t.nsecs*1e-9 - t0, 2)
    sonar_time.append(time)

bag.close()

### impact data
df1 = pd.DataFrame(list(zip(impact_time, impact_data)), columns=['time', 'impact'])
df1.to_excel(sav+'impact.xlsx', index=False)

### TENGs data
# df2 = pd.DataFrame(list(zip(teng_data1, teng_data2)), columns=['PDMS', 'Kapton'])
# df2.to_excel('/home/yxt/impact_data/6_21/good/tengs.xlsx', index=False)

df2_1 = pd.DataFrame(list(zip(teng_time1, teng_data1)), columns=['time', 'PDMS'])
df2_1.to_excel(sav+'pdms_tengs.xlsx', index=False)

df2_2 = pd.DataFrame(list(zip(teng_time1, teng_data2)), columns=['time', 'kapton'])
df2_2.to_excel(sav+'kapton_tengs.xlsx', index=False)

### torque data
df3 = pd.DataFrame(list(zip(torque_time, torque_data)), columns=['time', 'torque_y'])
df3.to_excel(sav+'torque_y.xlsx', index=False)

### Sonar data
df4 = pd.DataFrame(list(zip(sonar_time, sonar_data)), columns=['time', 'sonar'])
df4.to_excel(sav+'sonar.xlsx', index=False)




