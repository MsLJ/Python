# # -*- coding:utf-8 -*-
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing._data import MinMaxScaler
# from sklearn.neighbors._classification import KNeighborsClassifier
# df=pd.read_csv("C:/Users/soldesk/Desktop/자원2021/for AI/datingTestSet.txt",sep="\t",names=["비행기","게임","아이스크림","인기도"])
# print(df)
# 
# trainData=df[["비행기","게임","아이스크림"]].to_numpy()
# label=df["인기도"].to_numpy()
# 
# #비행기 마일리지:4만
# #게임: 최대100
# #아이스크림:일주일 동안 얼마나 먹는다고
# #=>게임/아이스크림은 별 영향을 못주고,비행기로 다 결정될것
# 
# #=>정규화(최대~최소 사이의 비율로 바꿔서)
# #각 항목별로 동등하게 영향 줄 수 있도록
# mms=MinMaxScaler()#정규화 해줄 객체
# trainData=mms.fit_transform(trainData)#학습 시키고 정규화
# 
# #항목이 몇개가 됐든 유클리드 거리로 구함
# knc=KNeighborsClassifier(20)
# knc.fit(trainData, label)
# 
# air=float(input("비행기 마일리지:"))
# game=float(input("게임하는 시간비율:"))
# ice=float(input("아이스크림 일주일에 몇개:"))
# predictData=np.array([[air,game,ice]])
# predictData=mms.transform(predictData)#그냥 정규화
# result=knc.predict(predictData)[0]
# print(result)
