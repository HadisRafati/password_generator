import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2,1,1)
plt.plot(x,y, linewidth = '3' , color = 'g', marker= 'o', mec= 'b', mfc = 'r')
plt.grid()
plt.title("Axis 1")


x = np.array([0, 10, 6, 3])
y = np.array([3, 80, 10, 1])
plt.subplot(2,1,2)
plt.plot(x,y, linewidth = '3', color = 'r', marker= 'o', mec= 'b', mfc = 'w')
plt.grid()
plt.title("Axis 2")

plt.suptitle("hadis")

plt.show()