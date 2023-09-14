# -*- coding:utf-8 -*-
from human import Human

class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def attack(self):
        print("공격")
    def show(self):
        print(self.name)
        print(self.age)
##############################
class IronMan(Avengers):
    # overriding? or overloading?
    def __init__(self, name, age, ai):
        # super.__init__(name,age) #Java스타일
        Avengers.__init__(self, name, age)  # Python스타일
        self.ai = ai
    def show(self):
        Avengers.show(self)
        print(self.ai)
######################################
# 헐크
# J: 다중상속X 그러다보니 Interface로 접근했던..
# P: 다중상속 가능
# 대부분의 언어들이 왜 다중상속을 못하게 만들어놨을까?
# ->다중상속을 하게된 경우 만약 Avengers쪽에서도 Show라는 메소드가 있는데
# Human쪽에서도 Show 메소드를 만들경우???
# 메소드명이 같으면? 어떤것의 메소드를 상속받은건지?
# -> 먼저 상속받은걸로 쳐줌
#    다중상속...?
class SpiderMan(Avengers, Human):
    pass
#########################################
# 다중상속 받았다->이름 나이 집주소
class CaptatinAmerica(Avengers, Human):
    def __init__(self, name, age, home):
        Avengers.__init__(self, name, age)
        Human.__init__(self, home)
        
    def show(self):
        Avengers.show(self)
        Human.show(self)
##############################
c=CaptatinAmerica("oldMan",70,"America")
c.show()
print("------------------------------")

#########################################

# 생성자가 상속됨
#    Avengers-이름,나이
#    Human-집 주소

############################################################
class Hulk(Avengers, Human):
    def __init__(self, name, age, stress):
        Avengers.__init__(self, name, age)
        self.stress = stress
    def show(self):
        Avengers.show(self)
        print(self.stress, "%")
#############################
s = SpiderMan("kimchi", 22)
s.attack()
s.eat()

print("-------------")
i = IronMan("torny", 30, "자비스")
i.attack()
i.show()
###############################
print("-------------")
h = Hulk("back", 43, 100)
h.attack()
h.show()
h.eat()


# p:생성자 상속됨
# overridng:몰려받은 메소드 재정의
# overloading:함수명 같게 파라메터명 다르게

# OOP:상속(상위클래스 기능몰려받고,기능 추가)
# 어벤져스
#    이름,나이
#    공격하기
#    정보출력
# 아이언맨
#    비서컴
