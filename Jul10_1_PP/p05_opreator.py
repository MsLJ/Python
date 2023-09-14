# -*- coding:utf-8 -*-

#+-*/%
x=int(input("x:"))
y=int(input("y:"))
print(x+y,x-y,x*y,x/y,x%y)
print("---------------------")

#J:Str+뭐->붙여서 Str
#P:숫자+글자 X안됌  (Str끼리만)
#print(x+"z")
print(x*y)
#J:숫자*String ==XX
#P: Str*숫자->반복
print(x*"ㅋ")
print("--------")
#J:int/int->int
#P:?/? ->알아서 소수점 살림 float
print(x/y)
#J에서 쓰던 /소수점 짜르는 나누기
print(x//y)
print("----------")

#+= -= /= *= %=
#x값 5증가
x+=5
print(x)

#++ -- 없음
#y값 1감소
#Python:효율성x,사람편한거
#    ->대체품이 있으면 삭제
#    ->공부할거리가 줄어듬
y=y-1   #9
y-=1    #6
#y--     #3 python에서는 이 문법이 없음
print(y)
