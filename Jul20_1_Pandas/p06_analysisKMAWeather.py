# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect
#OracleDB에 있는 기상청 날씨정보 df
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select*from kma_weather order by kw_date,kw_hour"
df=pd.read_sql(sql,con)
print(df)
print("-------")
#최고기온
print(df["KW_TEMP"].max())
print("-------")
#평균기온
print(df["KW_TEMP"].mean())
print("-------")
#최고기온 언제,몇시
print(df[df["KW_TEMP"]==df["KW_TEMP"].max()][["KW_DATE","KW_HOUR"]])
print("-------")
#평균기온보다 낮은거 언제,몇시,날씨
print(df[df["KW_TEMP"]<df["KW_TEMP"].mean()][["KW_DATE","KW_HOUR"]])
print("-------")

#sql로
sql="SELECT MAX(kw_temp)FROM kma_weather"
df=pd.read_sql(sql,con)
print(df)
print("-------")

sql="SELECT AVG(kw_temp)FROM kma_weather"
df=pd.read_sql(sql,con)
print(df)
print("-------")
sql="SELECT kw_date,kw_HOUR FROM kma_weather WHERE kw_temp in(SELECT MAX(kw_temp)FROM kma_weather)"
df=pd.read_sql(sql,con)
print(df)
print("-------")
sql="SELECT kw_date,kw_HOUR FROM kma_weather WHERE kw_temp <(SELECT AVG(kw_temp)FROM kma_weather)"
df=pd.read_sql(sql,con)
print(df)
print("-------")

con.close()



