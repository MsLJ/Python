# -*- coding:utf-8 -*-
import pandas as pd

#원본 수정을 안하려고-->~~작업해서 새 df만들기
df=pd.read_csv("C:/lee/kfoodPrice.csv",names=["어디","뭐","종류","가격","물건파는곳","지역"])

print(df)
print("---------")



print(df["뭐"].isnull())#값이 없나(T/F)
print(df[df["뭐"].isnull()])
print("---------")


#결측치->'없음'
df['뭐']=df['뭐'].fillna("없음")


#상품명에 사과 포함된거
print(df[df["뭐"].str.contains("사과")])
print("-----------")

#'없음' -> 결측
#pandas로 결측값이 표현 불가->numpy로
import numpy as np
df["뭐"]=df["뭐"].replace("없음",np.nan)
print(df[df["뭐"].isnull()])


