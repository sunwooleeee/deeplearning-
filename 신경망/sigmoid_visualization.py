from sigmoid import sigmoid_function
import matplotlib.pyplot as plt
import numpy as np 
x=np.arange(-5,5,0.1)
plt.plot(x,sigmoid_function(x))

plt.ylim(-0.1,1.1)
plt.show()