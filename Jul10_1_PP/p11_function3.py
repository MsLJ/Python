# -*- coding:utf-8 -*-
#printHab(10,20)
#printHab(10,200)
#printHab(100,200)
#메소드:객체의 액션
#함수:관련있는 작업을 묶어 정의 해놓고,
#     여러번 호출해서 쓰는
#    ->소스 정리
def printHab(a,b):
    print(a,b,a+b)

# def getHab(c,d):
#     return c+d 
# e=getHab(10, 30)
# print(e)   

#lambda :이름없음,1회용->값 간단하게 구하게 
#위의 함수처럼 계속 두고두고 쓰는게 아니라 1번쓰고 사라지는
#(lambda 파라메터1,파라메터2,...:내용)(값1,값2)
#내용자리에 단순한 식같은거 : return 

(lambda a,b:print(a,b,a+b))(10,20)
e=(lambda c,d:c+d)(10,30)
print(e)

# def calculate(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     f=a/b
#     return c,d,e,f
# g,h,i,j=calculate(100,3)
# print(g,h,i,j)

g,h,i,j=(lambda a,b:(a+b,a-b,a*b,a/b))(100,3)
print(g,h,i,j)
