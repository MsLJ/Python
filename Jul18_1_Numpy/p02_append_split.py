# -*- coding:utf-8 -*-
import numpy as np


a=np.random.randint(1,101,[3,5])
b=np.random.randint(1,101,[3,5])
print(a)
print(b)
print("--------")
d=np.concatenate([a,b])#붙이기
print(d)
print("-------")
e=np.append(a,b)#붙여서 1차원으로 -V 딥러닝&&인공신경망때 쓸것
print(e)
print("-------")
#Numpy,Pandas,TF,...
#axis=0:열 방향
#axis=1:행 방향
f=np.concatenate([a,b],axis=1)#붙이기
print(f)
print("-----")
g=np.append(a,b,axis=0)
print(g)
print("-----")
h=np.append(a,b,axis=1)
print(h)
print("=========")
aa=np.array_split(a,2)#대책없이 갯수 상관X2개로 나누기
print(aa)
# bb=np.split(b,2)#정확하게똑같이 2개로 나누기
# print(bb)#전체가 15개여서 2개로 못나눠서 에러
bb=np.split(b,3)
print(bb)

