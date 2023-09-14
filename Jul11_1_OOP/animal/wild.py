# -*- coding:utf-8 -*-


class pig:
    def __init__(self,name,age,kg):
        self.name=name
        self.age=age
        self.kg=kg


    def showInfo(self):
        print(self.name)
        print(self.age)
        print(self.kg)
        
################################################# 
if __name__=="__main__":#python의 main 
    from animal.pet import Dog
    d=Dog("둘리",2)
    d.showInfo()   
