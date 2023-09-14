# -*- coding:utf-8 -*-
from random import randint
from test.test_dis import outer

#JAVA
#for:반복횟수(0~10)
#for-each:컬렉션 탐색용
#while:반복조건
#do-while:반복조건(최소 1번은 반복 보장)

#jQuery
#$each();:JS배열 대상 for+for-each
#$(선택자).each();:DOM객체 대상 for+for-each
#int[]ar={1,2,3,4};
#for(int v: ar){
#}

#Python
#for-each:O
#while:O
#for:X없음

l=[1,2,3,4123,22,3,45]
for v in l:
    print(v)
print("----------")
#list,set,dict,range,tuple,...
#l2=[0,1,2,3,4]
#l2=range(5)#0~4
#l2=list(l2)
#기존 자바 for문처럼 쓰고싶으면 range쓰기
for v in range(5):
    print(v)
print("--------------")
for v in range(10,1,-1):
    print(v)
print("-------------")

for dan in range(2,10):
    print(dan,"단")
    for x in range(1,10):
        print(dan,"x",x,"=",dan*x,end="\t")
    print()    
 
#jQuery
#var ar=[1,23,234,1111];
#$.each(ar,function(i,v){
#});
#for v in enumerate(l3):#(인덱스,값)tuple상태로
#    print(v,type(v))
l3=['asda','vvv','qwe','zxc','aaaaaa']
for i,v in enumerate(l3): 
    print(i,type(i))
    print(v,type(v))
    print("---------")
print("===========")
#dict 순서X, 키-값 쌍=>for랑 연관X
d={"기온":30,"강수량":10,"습도":100}
for k,v in d.items():#(키,값) tuple로
    print(k,type(k))
    print(v,type(v))
    print("---------")
    
print("---------")
#1~10랜덤,5나오면 끝
#x=0 Java에서는 반복문 밖에 함수를 만들었는데 여기는 Interpreter방식이라 애초에 적용X
while (x!=5):
    x= randint(1,10)
    print(x)

        # continue
#반복문 속에서 변수 만들지 마시라 
#->Python&&Interpreter 방식에서는 안먹히는
#->효율적인 프로그램 X,개발용이O
#  

a=10
if a>5:
    b=20
#interpreter방식
#82번줄 돌아갈때 b가 있는거
print(b) 
 
print("--------")

j3=False
#내가 생각한건 숫자로 임의 변수값을줘서 for j문에 들어가면 숫자를 똑같이 하나씩 늘리는
#그리고 아래에 if문을쓰는
for i in range(6):
    for j in range(6):
        print(i,j)
        if j==3:
            j3=True
            break
    if j3:
        break
        #j->i
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
    
    
