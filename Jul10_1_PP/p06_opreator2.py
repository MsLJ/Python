# -*- coding:utf-8 -*-
name=input("이름:")
height=float(input("키:"))
age=int(input("나이:"))
print("-------------")
print("키는%.1fcm,나이는%d살"%(height,age))
print("-------------")

#키가 150이상
a=(height>=150)
print(a)

#J:연산자는 stack영역이 대상
#P:기본형이 없-> stack영역에 데이터가 없 ->?
#    알아서 적절히 돌아가게 되어있음

#이름이 홍길동
#자바에서 name=주소지값이 나오는데
b= (name=="홍길동")
print(b)

#and(&&),&
#or(||),|
#^ (조건에 하나만 적합할떄 xor)
#키가 100 넘고,나이가 80넘으면
c=(age>80) and (height>100)  
print(c)

#키가 100넘든지 나이가 80넘든지 하나만
d=(height>100)^(age>80)
print(d)

#20대만
#e=(age<30)and(age>19)
e=(19<age<30)
print(e)

#나이가 20살이 넘으면 어성세요 ,아니면 나가
#f=(age>=20) ? "어서오세요":"나가"
if(age>=20):
    print("어서오세요")
else:
    print("나가")
    
    
print(10<<2)    
