# -*- coding:utf-8 -*-
import pandas as pd

#원본 수정을 안하려고-->~~작업해서 새 df만들기
df=pd.read_csv("C:/lee/kfoodPrice.csv",names=["어디","뭐","종류","가격","물건파는곳","지역"])

# print(df)
print("---------")

 
print(df["가격"].max())
print(df["가격"].min())
print(df[df["가격"]==df["가격"].min()])
print("---------------")
print(df["가격"].mean())
print(df["가격"].median())#중앙값
print(df["가격"].sum())
print(df["가격"].count())
print(df["가격"].var())#분산
print(df["가격"].std())#표준편차
print("---------")
print(df["가격"].mode())#최빈값(제일 자주 나오는 값)=>Seriese
print(df["어디"].mode()[0])
print("------------")
print(df['가격'].decribe())#다
print(df.describe())#필드중에 숫자 있는거 알아서 다
