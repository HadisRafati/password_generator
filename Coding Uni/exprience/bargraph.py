import matplotlib.pyplot as plt
import numpy as np

y = np.array([164, 170, 132])
x = np.array(["Tehran", "Karaj", "Qazvin"])

plt.barh(x , y, color = 'pink')
plt.title("Hadis")
plt.ylabel("shahr")
plt.xlabel("Shakhes alodegi")

plt.show()