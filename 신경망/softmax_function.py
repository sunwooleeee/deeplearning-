import numpy as np 

def softmax_1(a):
    exp_a=np.exp(a)
    sum_exp_a=sum(exp_a)
    result=exp_a/sum_exp_a
    return result 

# 오버플로우 문제 발생 가능성 : 켬퓨터가 나타낼 수 있는 값의 범위 넘는 경우 발생 

def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=sum(np.exp(a-c))
    result = exp_a/sum_exp_a
    return  result

a=np.array([0.3,0.2,0.8])
print(softmax(a))
print(sum(softmax(a)))

