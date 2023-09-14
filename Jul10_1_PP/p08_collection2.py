# -*- coding:utf-8 -*-

#range 
a=range(10)#0~(10-1)
print(a)
print(type(a))

b= range(11)#0~10 리스트 만들기
b=list(b)
print(b)

c=range(2,10)#2~(10-1)
c=list(c)
print(c)

d=range(3,10,2)#3~(10-1),2칸씩
d=list(d)
print(d)

print("---------")

#tuple:데이터 여러개 용도X
#    특수한 용도 
e=(213,213,123,56,55)
print(e,type(e))
print(e[0])#list랑 무슨차이?

f=100
g=200
h=300
#변수 여러개 한번에 값 바꿀때 쓸수있음
(f,g,h)=(h,g,f)
print(f,g,h)
#변수 여러개 만들고 초기화
(i,j)=(99,88)
print(i,j)

#()생략가능
#(사실은 tuple쓴거지만) 변수 여러개 만들고 초기화 가능
k,l=1,2
print(k,l)

#가독성 적절히 봐가면서
height,weight=float(input("키:")),float(input("몸무게:"))
print(height)
print(weight)








