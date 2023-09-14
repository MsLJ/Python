# -*- coding:utf-8 -*-
import numpy as np
a=np.random.randint(1,11,[2,3])
print(a)
print("------")

b=np.sum(a)
print(b)

c=np.mean(a)
print(c)

d=a-c#각 값에서 평균 빼
d=d**2#제곱
d=np.mean(d)
print(d)

e=np.var(a)#분산
print(e)

f=np.sqrt(e)#분산에 루트
print(f)

g=np.std(a)#표준편차
print(g)

#분산/표준편차:평균에서 얼마나 벌어져있나

h=np.max(a)
print(h)
i=np.min(a)
print(i)

j=np.sum(a,axis=0)
print(j)
k=np.mean(a,axis=1)
print(k)
print("-----")
print(a)
print("-----")
l=np.argmax(a)#최댓값이 어디 있는지 index
print(l)
m=np.argmin(a)#최솟값이 어디 있는지 index
print(m)

#*중요*
n=np.argmax(a,axis=0)#열 방향 어느[]이 더 작은지
print(n)
o=np.argmin(a,axis=1)#행 방향
print(o)
print("----------")
p=np.cumsum(a)#행 방향으로 누적합
print(p)
q=np.cumprod(a)
print(q)#행 방향 누적곱
