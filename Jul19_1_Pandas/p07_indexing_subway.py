# -*- coding:utf-8 -*-
import pandas as pd
subwayDT=pd.read_csv("C:/lee/subway/subway.csv" ,names=["년","월","일","호선","역","탑승한 승객","하차한 승객"])
print(subwayDT)
print("-------")
#마지막 3개
print(subwayDT.tail(3))
print("-------")

# titanicDF.iloc[0:3]
print(subwayDT.head()[["년","월","일"]])#첫 5개 날짜
print("-------")
#10번~15번 데이터
print(subwayDT.iloc[10:16])
print("-------")
#20번 데이터 노선,역이름
print(subwayDT.iloc[20][["호선","역"]])
#몇호선 번호로찾을수있게 세팅
#2호선만
subwayDT=subwayDT.set_index(subwayDT["호선"])
print(subwayDT.loc["2호선"])
print("-------")
#3호선 역명 타고 내리고
print(subwayDT.loc["3호선"][["호선","역","탑승한 승객","하차한 승객"]])
print("-------")
#탄 사람수가 5만 넘는거
print(subwayDT[subwayDT["탑승한 승객"]>50000])
print("-------")

#내린 사람수가 100명 안되는거 년 월 일 노선 역

print(subwayDT[subwayDT["하차한 승객"]<100][["년","월","일","역"]])
#서울역
print(subwayDT[subwayDT["역"]=="서울역"])

# subwayDT=subwayDT.set_index(subwayDT["역"])
# print(subwayDT.loc["서울역"])
print("-------")
#역 이름에 '서울'이 들어가는거
#                    startswith
#                    endswith
#                    contains
print(subwayDT[subwayDT["역"].str.contains("서울")])
print("-------")

#역 이름에 '입구'들어가는거 노선 역명
print(subwayDT[subwayDT["역"].str.contains("입구")][["역","호선"]])
print("-------")

#for문으로 하나하나 나오게
#그냥 하나씩 다 값 받아서 tuple로 그리고 돌려도 하나씩 받을수있
# for v,v2,v3,v4,v5,v6,v7 in zip(subwayDT["년"],subwayDT["월"],subwayDT["일"],subwayDT["역"],subwayDT["호선"],subwayDT["탑승한 승객"],subwayDT["하차한 승객"]):
#     print(v,v2,v3,v4,v5,v6,v7)
# Shape를 사용
for i in range(subwayDT.shape[0]):
    print(subwayDT.iloc[i])
    print("-------------------")










