import matplotlib.pyplot as plt
import numpy as np

x = np.array(["apple", "blueberry", "cherry", "orange"])
y = np.array([40, 100, 30, 60])
colors = np.array(['y', 'b', 'r', 'g'])


plt.bar(x, y , color= colors)
plt.title("Friut supply by kind and color")
plt.ylabel("fruit supply")
plt.legend(title = "Fruit")

plt.show()