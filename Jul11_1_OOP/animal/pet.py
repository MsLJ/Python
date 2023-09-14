# -*- coding:utf-8 -*-
#import
#    Java타입:옵션사항->기본적으로 다른파일에 있는거 쓸수있는
#    Python타입:필수사항


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showInfo(self):
        print(self.name,self.age)
        
        
class Cat:
    def showInfo(self):
        print("고양이")        
#########################################
if __name__=="__main__":
    from animal.wild import pig
    p=pig("부대찌개",2,60)
    p.showInfo()
        
        
        
        
    print("ㅋ")
#Python의 import는 
#그 자리에 소스가 들어가는거
#main이 따로없는 interpreter방식언어
#=>그냥 실행 다 됨

#if__name__=="__main__":
#    여기서 실행했을때
#    import당했을때 말고
        
        
        
        
        
        
        