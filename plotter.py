import numpy as np 
import matplotlib.pyplot as plt 

plt.figure()
data = np.loadtxt('distance_time.txt')

plt.plot(data[:,1], data[:,0])
plt.title("Distance vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Distance (cm)")

plt.figure()
data2 = np.loadtxt('velocity_time.txt')

plt.plot(data2[:,1], data2[:,0])
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (cm/s)")

plt.figure()
data3 = np.loadtxt('pitch_time.txt')

plt.plot(data3[:,1], data3[:,0])
plt.title("Pitch vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Pitch (degrees)")
plt.show()