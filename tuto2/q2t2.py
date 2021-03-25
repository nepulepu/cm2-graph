import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10,0.001)
y=(2*x)/(x-3)
plt.ylim(-10,10)
plt.plot(x,y)
plt.show()