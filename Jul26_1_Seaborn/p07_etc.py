# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect
from json import loads
from _datetime import datetime
from pandas.io.sql import read_sql
from http.client import HTTPConnection


fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

huc=HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
rb=huc.getresponse().read()
print(rb.decode())
huc.close()
dustData=loads(rb)["RealtimeCityAir"]["row"]
df=pd.DataFrame(dustData)
#scatter+회귀(주어진 점들 최대한 만족시킬만한 직선)
# sns.lmplot(data=df,x="PM10",y="PM25",col="MSRRGN_NM")

#scatter+hist
# sns.jointplot(data=df,x="PM10",y="PM25")
# sns.jointplot(data=df,x="PM10",y="PM25",kind="reg") #회귀선까지
# sns.jointplot(data=df,x="PM10",y="PM25",kind="kde") #등고선으로
sns.jointplot(data=df,x="PM10",y="PM25",kind="hex") #육각형으로
plt.show()



