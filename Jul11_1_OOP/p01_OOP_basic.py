# -*- coding:utf-8 -*-


# J:Perfect OOP
#    package(필수)>class.java(필수)
# P:Hybrid OOP->객체지향 안하려면 안하는거
#        1 file=1 module
#    packae(안해도) >module(필수) > class(안해도)

#OOP
#    1file=1class

#클래스명을 대문자로 시작:Java진영
#c#
# 클래스명 대문자로 시작안해도 상관X
# 접근제어자 없음 ->캡슐화도 없고 패턴프로그래밍 없음
class Dog:
    name=None
    age=None
    
    def bark(self):#메소드는 첫번째 파라메터로 self
        print("mung")
    def printInfo(self):
        print(self.name)
        print(self.age)
        print(self.type)
#######################
d=Dog()#def함수를 부른것인지,class를 부른것인지 분간 불가능 class도 소문자를 사용할수있기에 방법이없다..
d.name="후추"
d.age=13
d.type="sibagyun"#클래스 외부에서 멤버변수 추가 가능
#Python (클래스명.xxx(객체))
Dog.bark(d)
Dog.printInfo(d)
# 대부분 PL들의 Java스타일(객체.xxx())
d.bark()#메소드 호출때는 self는 없는취급
d.printInfo()








