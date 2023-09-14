# -*- coding:utf-8 -*-
import pandas as pd

df=pd.read_csv("C:/lee/work space/titanic.csv")
print(df)
print("---------")
print(df.columns)
print("--------")
df= df.set_index(df["Name"])
print(df)
print("--------")
#index기준 정렬(a,b,c순)
df= df.sort_index()
print(df)
print("--------")
#index기준 정렬(내림차순)
df=df.sort_index(ascending=False)
print(df)
print("--------")

#행 하나를 필드명 abc순 정렬(필드명 정렬)
df=df.sort_index(axis=1)
print(df)
print("--------")

#특정 필드 기준 정렬
df=df.sort_values(by="Age")
print(df)
print("--------")

df=df.sort_values(by="Pclass",ascending=False)
print(df[["Name","Pclass"]])
print("------")

#좌석등급 내림차순 ->나이 오름차순

df = df.sort_values(by=["Pclass", "Age"], ascending=[False, True])
print(df[["Pclass", "Age"]])











