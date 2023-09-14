# -*- coding:utf-8 -*-
import numpy as np


a=np.random.randint(1,11,[2,3])
b=np.random.randint(1,11,[2,3])
c=a+b#연산자로 하면 되는데
print(c)#method도 있다
print("----------")
d=np.add(a,b)
e=np.subtract(a,b)
f=np.multiply(a,b)
g=np.divide(a,b)
p=np.mod(a,b)#%
i=np.power(a,b)#제곱
print(d)
print(e)
print(f)
print(g)
print(p)
print(i)
print("------")
j=a>b
print(j)
print("____")
#greater,greater_equal
#less,less_equal
#equal,not_equal
k=np.greater(a,b)
print(k)
print("-------")
name=np.array(["hongcha","leesanghannala","kimchi"])
kor=np.array([100,90,80])
eng=np.array([10,60,70])
mat=np.array([30,40,50])
avg=np.divide(np.add(kor,eng,mat),3)
# avg=(kor+eng+mat)//3  
#평균 50넘는 학생이름
# np.greater(avg,50)
print(name[np.greater(avg,50)])

print("-----")
print(a)
print(b)
print("-----")
l=np.maximum(a,b)#각 자리별 큰 값
print(l)
m=np.minimum(a,b)
print(m)
n=np.random.rand(2,3)
print(n)
o=np.ceil(n)#소수점 이하 올림
print(o)
p=np.floor(n)#소수점 자르기
print(p)
q=np.rint(n)#소수점 이하 반올림
print(q)
r=np.round(n,2)#소수점 이하 2자리 반올림
print(r)
#소수점 이하 셋째자리에서 올림
s=np.ceil(n*100)/100
print(s)
#np.nan없음
#np.inf 무한
t=np.array([12,34,1,np.nan,np.inf,43])
print(t)

