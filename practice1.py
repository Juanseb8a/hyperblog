import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Basics of plotting
x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

plt.plot(x,z)
plt.plot(x,y)

plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")

plt.legend(["this is z", "this is y"])
plt.show()

