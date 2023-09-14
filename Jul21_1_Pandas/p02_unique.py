# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect
#타이타닉
df=pd.read_csv("C:/lee/work space/titanic.csv")
print(df)
print(df.columns)
#좌석 클래스별 요금 평균가 Pclass  Fare
# df.groupby("Pclass")["Fare"].mean()
print(df.groupby("Pclass")["Fare"].mean())
print("----------------------")
#좌석 클래스별 죽은사람수/산사람수 Pclass Survived
print(df.groupby(["Pclass","Survived"])["PassengerId"].count())
print("----------------------")
#성별 별로 죽은사람수/산사람수Sex Survived
print(df.groupby(["Sex","Survived"])["PassengerId"].count())
print("----------------------")
#객실명이 뭐있나(중복제거)
print(df["Cabin"].unique())
print("----------------------")
#객실이 몇개 있었나
print(df["Cabin"].nunique())
print("----------------------")

#객실별로 몇명씩
print(df["Cabin"].value_counts())

#ORacleDB기상청
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="SELECT *FROM kma_weather"
df2=pd.read_sql(sql, con)
con.close()
print(df2)
print("--------")
#어떤 날씨들이 있었나
#대/소문자 구별해서 소문자로 넣으면 인식X
print(df2["KW_WFKOR"].unique())
print(df2["KW_WFKOR"].nunique())
print("--------")

#각 날씨별 맑음은 몇번
print(df2["KW_WFKOR"].value_counts())
print("--------")



