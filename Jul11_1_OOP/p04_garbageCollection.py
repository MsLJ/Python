# -*- coding:utf-8 -*-
#Garbage collection  
#heap에서 주소지,객체를 생성하고 그걸 stack영역에 끌어다 쓰는데 그 stack영역에서 heap영역에 있는 주소값을
#쓰이는곳이 없으면 알아서 지워주는
from tkinter.messagebox import showinfo

class Garbage:
    name=None
    recycle=None
    
    def __init__(self):
        print("쓰레기 생성")
    def __del__(self):
        print("쓰레기 소멸")

    def showInfo(self):
        print(self.name)
        print(self.recycle)
        
g=Garbage()
g.name="에어컨"
g.recycle=False
g.showInfo()
g2=Garbage()
g2.name="재활쓰"
g2.recycle=True
Garbage.showInfo(g2)
g3=g
g3.name="에어컨+전기줄"
g3.recycle=False
g3.showInfo()
g.showInfo()
g=None#주소지 끊기
g3=None#주소지 끊기 Gc작동
#g2=None
print("zzzzzz")#프로그램이 종료되는시점


#    Static/stack:프로그램 종료되면 메모리 정리
#    heap:메모리는 수동으로 정리해야
#Garbage Collection:heap영역 자동정리 시스템
#     그 자동이 언제 :그 주소값 더이상 못쓰게 돼면 더이상 그 객체의 주소값에 접근하지 못하게돼면
#    Java/Python개발자는 메모리 관리 몰라도

#     BD/AI

























