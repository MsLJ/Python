# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect
from http.client import HTTPConnection
from json import loads


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
# sns.histplot(data=df,x="PM10",palette="summer")
# sns.pairplot(data=df,palette="summer")
#젤 이뻐서 많이씀
# sns.violinplot(data=df,x="PM10",palette="summer")
sns.violinplot(data=df,x="MSRRGN_NM",y="PM10",palette="summer")
plt.show()