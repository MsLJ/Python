# -*- coding:utf-8 -*-

# 메뉴
# 메뉴명이 김치찌개
# 가격이 9000원
# 정보 출력
class Menu():
    name = None
    price = None
    
    # constructor(생성자)
    #    overloading이 안되니 ->생성자는 하나만 가능
   # def __init__(self):#__init__=파이썬의 생성자
       # print("메뉴 객체 만들어짐")
       # print("생성자 전혀 건들지 않으면 자동으로")
        
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    # destructor (소멸자)
    def __del__(self):  # 생성자와 반대되는 이 메뉴객체가 사라질때
        print("메뉴객체없어짐")    
        
        
        
        
    def printInfo(self):
        print(self.name)
        print(self.price)
# 멤버변수는 써봐야 의미가 없고 (외부에서 넣을수이ㅣㅆ으니)
# 메소드는 정해진대로 쓰고
# Overloading이 안되니 생성자는 하나만 가능하고
# =>생성자에서 멤버변수를 결정하는 경향이
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def showInfo(self):
        print(self.name)
        print(self.price)


p = Product("샴푸", 9000) 
p.showInfo()      
m = Menu("김치찌개", 9000)
m.printInfo()      



# Garbage Collection  
