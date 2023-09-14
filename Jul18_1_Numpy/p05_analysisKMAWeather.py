# -*- coding:utf-8 -*-
import numpy as np

f=open("C:/lee/kmaweahter.csv", "r", encoding="utf-8")
#시간별 평균 기온
#dict를 두개 만들껀데 일단 시간별로 온도를 다 더하는거랑
#그 시간대가 몇개인지 세는거? 그렇게 2개의 dict 그래서
#그 온도 다 더한거랑 그 시간대 세놓은 벨류 나눠서 평균구하기 
hourstemp={"12":0,"15":0,"18":0,"21":0,"24":0}
hoursCount={"12":0,"15":0,"18":0,"21":0,"24":0}
weatherDict={}
# hours=[]
# temp=[]
# count=[]
for l in f.readlines():
    l=l.replace("\n","")
    l=l.split(",")
    hourstemp[l[3]]+=float(l[4])
    hoursCount[l[3]]+=1
    
for k,v in hourstemp.items():
    weatherDict[k]=v/hoursCount[k]
#     hours.append(k)
#     temp.append(v)
#     count.append(hoursCount[k])


for k,v in weatherDict.items():
    print(k,v)




# print(hours)
# print(temp)
# print(count) 
# hours=np.array(hours)
# temp=np.array(temp)
# count=np.array(count)
# avgtemp=temp//count

# print(hourstemp)
# print(hoursCount)
f.close()
###########################
#제일 추운거 몇시
#제일 더운거 몇시
#총 평균기온
#총 평균기온보다 더운거 몇시
hours=[]
temps=[]
for k,v in weatherDict.items():
    hours.append(k)
    temps.append(v)
    
print(hours)
print(temps)
hours=np.array(hours)
temps=np.array(temps)
#젤 추운거
l=np.argmin(temps)
print(l)
print(hours[4])

#젤 더운거
##argmin이랑argmax를 하는데 만약에 값이 같으면 둘다 안뜨고 하나만 출력돼는 
##그럼 동점상황에서는 어떻게  해야할까? 
##true false를 사용
print(temps==np.max(temps))
l=np.argmax(temps)
print(hours[temps==np.max(temps)])
print(temps[temps==np.max(temps)])
# print(hours[1])

#총 평균기온
sumavgtemp=np.mean(temps)
print(sumavgtemp)

#총 평균기온보다 더운거 몇시
print(hours[temps>sumavgtemp])
for h in (hours[temps>sumavgtemp]):
    print(h)

