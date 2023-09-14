# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads
#서울시 실시간 미세먼지->pd.DataFrame
huc=HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody=huc.getresponse().read()
# print(resBody)
mungi=loads(resBody)
#그냥 이거 들가고나면 데이터가 한줄에있으니까 그거 그냥 바로 DataFrame하면 끝
mungiDF=pd.DataFrame(mungi["RealtimeCityAir"]["row"])
print(mungiDF)
huc.close()
