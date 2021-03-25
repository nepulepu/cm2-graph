import matplotlib.pyplot as plt
x=[]
i=-5.0
while i <= 5:
    x.append(i)
    i+=0.1
#x=[i for i in range(-5,5)]
y=[abs((i*i)-1) for i in x]
plt.plot(x,y)
plt.show()