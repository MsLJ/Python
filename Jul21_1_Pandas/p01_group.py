# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect
#물가정보
df=pd.read_csv("C:/lee/kfoodPrice.csv",names=["어디","뭐","종류","가격","시장","구"])
print(df)

print("______________________")

# print(df["가격"].mean())#평균가
# #종류별 평균가
# print(df.groupby("종류")["가격"].mean())
# print("-------")
# #구별 최고가
# print(df.groupby("구")["가격"].max())
# 
# #구별 ->종류별 최고가
# print(df.groupby(["구","종류"])["가격"].max())
# print("----------------")

#OracleDB에 있는 기상청데이터
#날씨별 평균기온
#SELECT KW_WFKOR,avg(kw_temp) FROM kma_weather GROUP BY KW_WFKOR

#Pandas버젼
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="SELECT *FROM kma_weather"
df2=pd.read_sql(sql,con)
print(df2.groupby("KW_WFKOR")["KW_TEMP"].mean())
print("-----------")
#SQL 버젼
sql="SELECT KW_WFKOR,avg(kw_temp) FROM kma_weather GROUP BY KW_WFKOR"
df2=pd.read_sql(sql,con)
print(df2)
con.close()
















