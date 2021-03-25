import matplotlib.pyplot as plt
import numpy as np
import math

x=np.arange(-5,5,0.0001)
y=1/x
plt.ylim(-10,10)
plt.plot(x,y)
plt.show()