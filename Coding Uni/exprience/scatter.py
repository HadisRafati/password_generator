import matplotlib.pyplot as plt
import numpy as np

height = np.array([160,175,170, 163, 170])
weight = np.array([60, 75, 77, 50, 70])
colors = np.array(["red","green","blue","yellow","pink"])

plt.scatter(height,weight , c = colors , alpha = 0.5)




plt.show()