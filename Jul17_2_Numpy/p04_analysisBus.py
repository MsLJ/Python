# -*- coding:utf-8 -*-
#일단 년도는 어차피 같아서 상관X
#그러면 line.split(",")하고 [0]은 필요없을거고
#근데 요일 구하려면 필요하고
#요일은 구했으니 이제 같은 버스와 요일을 넣으면 될것
#[3]은 버스 번호 [4]에는?
#애초에 데이터 만들때 실수로 ,를 안찍어서 split이 이상하게 나오는거였다 ㅋㅋ
#다시 확인좀 하자 꼼꼼히...
#그러면 ridedict{youil:[4]}버스번호:승객수
#alightdict{youil:[5]}를 생각했는데
#문제발생

#탄 < 내린요일
# bd=datetime.strptime(bd,"%Y/%m/%d")
# bda=datetime.strftime(bd,"%A")
from _datetime import datetime
f = open("C:/lee/busData2015.csv", "r", encoding="utf-8")
#어차피 요일 다 아니까 그냥 요일들 dict에 넣어주는건 우리가 수동으로하자
#    만약 이것보다 더 큰 데이터였다면
#     컴퓨터가 하게돼면 컴퓨터가 과부화 오게될것
rideDict={"Sunday":0,"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0}
alightDict={"Sunday":0,"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0}

youilBusRide={}
youilBusAlight={}
#C:\lee 파이썬에서 파일경로에 역슬래쉬X 그냥 슬래쉬 쓸것
for l in f.readlines():
    l=l.replace("\n","").split(",")
    day=datetime.strptime(l[0]+l[1]+l[2],"%Y%m%d")
    youil=datetime.strftime(day,"%A")
    #print(l)
    #우리가 기존 방식으로 하지않고 리스트 순을 역으로 쓴 이유:
    #->기존 방식으로 하게될경우 우리가 split을,로 하게됐는데 이 데이터내에 ,,를 여러개찍어놓은 데이터가 있기에
    #->그 split으로 해서 그냥 5번째 6번째 이렇게 할경우 5,6번째에 숫자가아닌 문자가 나오게됌
    #한마디로 Parsing이 제대로 안돼서 
    #역으로 생각하면 될것 어차피 마지막에서 마지막에서 첫번째가 내린 승객인원수이고 마지막에서 두번째가 탑승한 인원 승객수일테니
    rideDict[youil]+=int(l[-2])
    alightDict[youil]+=int(l[-1])
youils,rides,alights=[],[],[]
for k,v in rideDict.items():
    youils.append(k)
    rides.append(v)
    alights.append(alightDict[k])
print(youils)
print(rides)
print(alights)
import numpy as np 
youils=np.array(youils)
rides=np.array(rides)
alights=np.array(alights)
print(youils[rides<alights])

    
        

    
f.close()
