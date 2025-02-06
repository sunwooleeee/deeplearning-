import numpy as np
A=np.array([1,2,3,4])
print(A)
# 차원 확인
print(np.ndim(A))
#배열 구조 확인
print(A.shape)
#첫번째 인자 배열 확인 
print(A.shape[0])

B=np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
print(B.shape)