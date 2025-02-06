import numpy as np
import sigmoid 
# x: 입력층
x=np.array([1,0.5])
# w : 가중치 
w1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
w2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
w3=np.array([[0.1,0.3],[0.2,0.4]])
# b : 편향 
b1=np.array([[0.1,0.2,0.3]])
b2=np.array([[0.1,0.2]])
b3=np.array([[0.1,0.2]])

a1=np.dot(x,w1)+b1
a2=np.dot(a1,w2)+b2
a3=np.dot(a2,w3)+b3

print(a3)