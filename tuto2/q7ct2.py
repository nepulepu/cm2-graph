import matplotlib.pyplot as plt
import numpy as np
import math

x=np.arange(0,5,0.0001)
y=math.e**x
plt.plot(x,y)
plt.show()