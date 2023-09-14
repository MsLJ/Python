# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect
#OracleDB에 있는 owm날씨 불러서
#기온,습도,꺾은선 그래프
#날짜를 "23일 10시" 형태로
fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select*from weather_Data"
df=pd.read_sql(sql,con)
print(df)
con.close()
df=df.sort_values(by="W_DATE")
print(df)
def convert(d):
    return "%d일 %d시"%(d.day,d.hour)

df["W_DATE"]=df["W_DATE"].apply(convert)
print(df)
#Pandas DF=>Numpy Array
# a=df.to_numpy()
# print(a)

date=df["W_DATE"]
temp=df["W_TEMP"]
humi=df["W_HUMDITY"]
_, cf1=plt.subplots()
p1=cf1.plot(date,temp,"r-")
cf1.set_xlabel("언제")
cf1.set_ylabel("기온")

cf2=cf1.twinx()
p2=cf2.plot(date,humi,"b-")
cf2.set_ylabel("습도")
cf1.legend(p1+p2,["기온","습도"])
plt.title("날씨")
plt.show()