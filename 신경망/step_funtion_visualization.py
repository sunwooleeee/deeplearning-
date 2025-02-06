from step_function_array_Ver import step_function_array
import matplotlib.pyplot as plt 
import numpy as np
x=np.arange(-5,5,0.1)
y=step_function_array(x)

plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()