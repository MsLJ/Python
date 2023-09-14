# -*- coding:utf-8 -*-


#1)함수 정의
#def 함수명(변수명=기본값,변수명=기본값,...):
#        내용
#        return 값
def gamza():
    print("슈퍼 가서")
    print("감자 사와")
  
def test():
    print("ㅋ")
    
    
# : 뒤에 무조건 들여쓰기가 들어가야    
def test2():
    pass #들여쓰기 자리 차지 개발중에 쓸게없으면 쓰는  안쓰면 오류

def printHab(x=1,y=2):
    print(x)
    print(y)
    print(x+y)
    

def funcTest(a=10,b=20,c=30):
    print(a,b,c)
    
#overridng vs 
#overloading:함수명 같게,파라메터 다르게
#함수 기본값/자료형 안쓰고 ->overloading없음
#오버로딩(Overloading)은 기존에 없던 새로운 메서드를 정의하는 것이고,
#오버라이딩(Overriding)은 상속 받은 메서드의 내용만 변경 하는 것이다.

#정수 2개넣으면 더 큰 숫자 출력하는 함수
def biggernum(x=10,y=20):
    pass
        
#정수 3개 넣으면 가장 큰거 출
def biggernum2(x=10,y=20,z=30):
    pass

#함수 1->결과 1
#함수 1->결과 n

#정수 2개넣으면 합 구하기
#Python은 함수하나에서 리턴 여러개?X
#단지 Tuple의 특성을 활용한것뿐
def calculate(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d

#문장 하나 넣으면,첫번째글자/마지막글자 구하는
def munzang(a):
    return a[0],a[-1]   
    #사실은tuple하나->리턴 여러개같이 생김
#######################################
a,b=munzang("kimchi")
print(a)
print(b)
#변수 생성하기싫고 받기 싫으면_쓰기
a,_=munzang("kimchi")
#2)함수호출  영역 구분이 없고 메인도 없어서 그냥 부르면됌
# 함수명(값,값,...)
# 함수명(변수명=값,변수명=값,...)
#aa=calculate(10, 20)
#print(aa)
aa,bb,cc,dd=calculate(30, 50)
print(aa)
print(bb)
print(cc)
print(dd)


gamza()
test()
printHab(10, 30)
printHab(y=100, x=50)
printHab()
printHab(y=10)
funcTest()
funcTest(b=200, c=300,a=100)
funcTest(1000,c=3000)

biggernum(30, 1)

