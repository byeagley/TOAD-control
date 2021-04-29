import numpy as np 
import matplotlib.pyplot as plt 

plt.figure()
data = np.loadtxt('distance_time.txt')

plt.plot(data[:,1], data[:,0])
#plt.show()

plt.figure()
data2 = np.loadtxt('velocity_time.txt')

plt.plot(data2[:,1], data2[:,0])
plt.show()