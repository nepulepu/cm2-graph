import math
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-1*np.pi,np.pi,0.0001)

plt.plot(x,np.tan(x))
plt.ylim(-10,10)
plt.show()