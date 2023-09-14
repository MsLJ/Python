# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from http.client import HTTPConnection
from json import loads
fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용

#서울 실시간미세먼지
#구별로 미세 +초미세 막대 그래프
huc=HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody=huc.getresponse().read()
print(resBody.decode())

huc.close()
dustData=loads(resBody)
dustData=dustData["RealtimeCityAir"]["row"]
dustDF=pd.DataFrame(dustData)
print(dustDF)

gu=dustDF["MSRSTE_NM"]
pm10=dustDF["PM10"]
pm25=dustDF["PM25"]

plt.bar(gu,pm10,color="red")
plt.bar(gu,pm25,color="blue",bottom=pm10)
plt.show()
