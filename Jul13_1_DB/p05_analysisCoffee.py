# -*- coding:utf-8 -*-
from cx_Oracle import connect

# csv 불러서 coffee객체 list로

#Coffee클레스를 만들고 거기서
class Coffee:
    #그냥 라인을 넣어주고 그 라인에 스플릿해서 배열 네임을[0] 카테고리[1] 가격[2]
    def __init__(self,line):
        line=line.split(",")
        self.name=line[0]
        self.cate=line[1]
        self.price=line[2]
        
    def show(self):
        print(self.name,self.cate,self.price)








f = open("C:/lee/0713.csv", "r", encoding="utf-8")
coffees=[]
for  l in f.readlines():
    l = l.replace("\n", "")
    c=Coffee(l)
#    c.show()
    coffees.append(c)

    # print(l)
#########################################
#1)평균가
pp=0
#count객체를 만들게아닌 length로 나누면 될것
for p in coffees:
    pp+=int(p.price)
avgp=pp//len(coffees)
    
print(avgp)
#2)메뉴 총 몇 종류
# count=0
#count객체를 만들게아닌 length를 쓰면될것
# for c in coffees:
#     count+=1
#     print(c.cate)
    
    
print(len(coffees),"종류")
print("---------")




#3)최고가 메뉴 뭐/최저가 메뉴 뭐
coffees.sort(key=(lambda cf:cf.price),reverse=True)
coffees[0].show()
coffees[-1].show()    

f.close()







