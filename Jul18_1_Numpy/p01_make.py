# -*- coding:utf-8 -*-
import numpy as np

#tensorflow 등 후속기술에서 사용
#->인공신경망 초기값
#더미데이터 만들때

a=np.zeros([3,2])#3x2 0들
print(a)
b=np.ones([3,2])#1들
print(b)
c=np.empty([3,2])#의미 없는값들
print(c)
e=np.arange(2,6)
print(e)
f=np.arange(2,10,3)
print(f)
print("-------")

g=np.random.rand(3,2)#0.0부터~0.99까지 3*2
print(g)

h=np.random.randn(3,2)#평균0,표준편차1 랜덤 3x2
print(h)

i=np.random.randint(2,10,[3,2])#2~(10-1)까지 랜덤한 숫자3x2
print(i)

















