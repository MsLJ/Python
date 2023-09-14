# -*- coding:utf-8 -*-
import numpy as np 
f=open("C:\lee\subway\subway.csv","r",encoding="utf-8")
name1=[]
ride=[]
ad=[]
rideDict={}
alightDict={}
#name=서울역
#ridesum=10만,20만
#alightSum=15만,30만
#오답노트
#set을 사용하면 중복은 제거가 돼는데 순서도 뒤죽박죽에 
#그 중복이 제거됐을때 기존에 같은 크기의 list의 탑승한 승객의수,내린 승객의수 리스트의 크기가 다 달라지기에..
#몇번째의 리스트가 제거됐는지도 모름 그러면 set은 아니겠고 아니면 set을 하대 다른 작업이 필요?
#반복문을 활용해야할꺼같은데 
#->dict를 활용하자 dict를 활용해서 if를 사용해서 그 키 값이 없을때는 그냥 그 값을 그대로
#    키 값이 중복될때는 그 값을 더하는 형식으로
#    그런 형식으로 중복된걸 해결 그리고 이렇게 하면 어차피 크기도 같을테니
#    그냥 네임,승객 탑승한수,내린수를 list에 담고 numpy를 사용하면 될것
for line in f.readlines():
    line=line.replace("\n","").split(",")
    if line[4]in rideDict:
        rideDict[line[4]]+=int(line[5])
        alightDict[line[4]]+=int(line[6])
        
    else:
        rideDict[line[4]]=int(line[5])
        alightDict[line[4]]=int(line[6])
for k,v in rideDict.items():
    #print(k,v)
    name1.append(k)
    ride.append(v)
for k,v in alightDict.items():
    ad.append(v)
   
f.close()

# print(n1)
# print(r1)
# print(ad)
name=np.array(name1)
rideSum=np.array(ride)
alightSum=np.array(ad)
#print(name)
print(name[rideSum<alightSum])
    



