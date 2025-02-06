import numpy as np
def step_function_array(x):
    y=x>0
    return y.astype(int)

x=np.array([-1.0,1.0,2.0])
print(step_function_array(x))