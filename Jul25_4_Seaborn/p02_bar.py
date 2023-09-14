# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect, Connection
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용

#실시간 미세먼지 pd.df


huc=HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody=huc.getresponse().read()
huc.close()

dustData=loads(resBody)["RealtimeCityAir"]["row"]
df=pd.DataFrame(dustData)
# print(df)

# sns.barplot(data=df)#pd.DataFrame알아서 그리기는 함
#통계가 필요하면 알아서(권역별 PM10평균)
#검은선: 신뢰구간 95%
# sns.barplot(ci="sd",x="MSRRGN_NM",y="PM10",data=df,palette="Pastel1")

#갯수
# sns.countplot(x="MSRRGN_NM",data=df,palette="autumn")

#권역별 데이터 몇개씩, 상태별로 색깔 다르게 표현
# sns.countplot(x="MSRRGN_NM",hue="IDEX_NM",data=df,palette="autumn")
# plt.show()


#OracleDB에 있는 기상청 날씨
#시간대별 데이터 몇개씩
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select * from kma_weather order by kw_date,kw_hour"
df2=pd.read_sql(sql,con)
con.close()
print(df2)

# sns.barplot(x="KW_HOUR",y="KW_TEMP",data=df2,palette="rocket")
#sns.barplot(x="KW_HOUR",y="KW_TEMP",data=df2,palette="rocket")

#시간대별 데이터 몇개씩
sns.countplot(x="KW_HOUR",hue="KW_WFKOR",data=df2,palette="Accent")

plt.show()



