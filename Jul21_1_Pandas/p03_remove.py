# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect
df=pd.read_csv("C:/lee/work space/titanic.csv")
print(df)
print("------------")

#삭제가 의미X
#    -원본 안건드는
#    -삭제X 나머지 추출o

#필드 삭제
print(df.columns)
df=df.drop("PassengerId",axis=1)
df=df.drop(df.columns[0],axis=1)
df=df.drop(["Pclass","Name"],axis=1)
print(df)
#성별 나이만 빼고 나머지 다 삭제->성별,나이만 추출

df=pd.read_csv("C:/lee/work space/titanic.csv")
print(df)
print("------")

#데이터 삭제
df=df.drop(0)#행,번호로 지우기-x ,index로 지우기
df=df.set_index(df["Pclass"])#객실등급으로 찾기
df=df.drop(3)#객실등급이 3등급인거 다 지우기
print(df)



#df=df.set_index(df["Sex"])
#df=df.drop("male")
df=df[df["Sex"]=="female"]
print(df)
print("-------")

#OracleDB에 오픈웨더맵
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="SELECT *FROM weather_Data"
df2=pd.read_sql(sql, con)
print(df2)
print("-----------")
#습도필드 제거하고
# df2=df2.drop("W_HUMDITY",axis=1)
# print(df2)
#날짜 기온 날씨 순으로 보이게 필드 정렬
#제거 안하고 그냥 필요한것들만 갖고오기
df2=df2[["W_DATE","W_TEMP","W_DESCRIPTION"]]
print(df2)
#평균기온보다 낮은 데이터 제거
df2=df2[df2["W_TEMP"]>=df2["W_TEMP"].mean()]

#다 조회
print(df2)
#결론 그냥 삭제는 별 의미X 그냥 갖고오고싶은 데이터만  가져오면 될것





