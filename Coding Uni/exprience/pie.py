import matplotlib.pyplot as plt
import numpy as np

y = np.array([19, 56, 46, 22, 26])
myexpload = [0.3 , 0, 0, 0, 0]
mylable = ["Hadis", "Pedar", "Madar", "Kosar", "Hamid"]

plt.pie(y, explode = myexpload, labels= mylable)
plt.legend(title = "My Family")
plt.title("Age")
plt.show()