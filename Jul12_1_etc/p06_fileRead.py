# -*- coding:utf-8 -*-
#open (경로,모드
#                        r
#                        w
#                        a
#                        
ff=open("C:/lee/0712.txt","r",encoding="utf-8")
# a=ff.read()#전체 다 읽어서, str하나로 
# print(a)
# print(type(a))

# b=ff.readline()#다음 한 줄 읽어서,str하나로
# print(b)
# b=ff.readline()
# print(b)

#HDD에 1TB->               RAM
#전체 다 읽어서,엔터키 기준으로 나눠서 list
# c=ff.readlines()
# print(c)
# print(type(c))

for l in ff.readlines():
    l=l.replace("\n","")
    print(l)


ff.close()

