import matplotlib.pyplot as plt
import numpy
x=[i for i in range(1,50)]
y=[20*i**3+180/i for i in x]

plt.plot(x,y)
plt.show()