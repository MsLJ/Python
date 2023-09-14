# -*- coding:utf-8 -*-

#Java: 규칙->소스보기 편함
#        저급언어->컴퓨터 친화적(효율적인 프로그래밍 가능)
#Python:자유 ->복잡해짐
#        고급언어-> 사람 친화적(개발이 편한)

#Java:저급언어(사람이 컨트롤)
# 데이터 특징 파악해서 최적의 자료형찾기

#Python : 고급언어 (언어 자체적으로 자동 처리)
#   자료형 자동
#    기본형X,전부 다 객체

#Python int = Java의 Integer(int가 아님)
a=10# a 변수 만들고 10
#for():
   # a=20 #변수 만들고 20? 아니면 기존에 a가 20?
print(a)#Object a=new Integer(10);
print(type(a))#자료형 뭔지 확인
print(id(a))#Heap영역 주소값 변수가 전부다 객체형이라 Heap에 주소지 
#생성 이후 Stack에 가져다 오는 그만큼 메모리 낭비가 많다.
a="q" #a=new String("q");
print(a)
print(type(a))
print(id(a))

#interpreter
#Java시절에 변수 사용범위가 어쩌고...-x
#그 변수 쓰는 시점에 그 변수가 있기만 하면 o
a=20
if(a>10):
    b=30
print(b)    