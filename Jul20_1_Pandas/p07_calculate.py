# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads

#서울 실시간 미세먼지 df
huc=HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
ResBody=huc.getresponse().read()
print(ResBody.decode())
huc.close()

dustData=loads(ResBody)
df=pd.DataFrame(dustData["RealtimeCityAir"]["row"])
#권 , 구, pm10,pm25,상태
# print(df["MSRRGN_NM"],df["MSRSTE_NM"],df["PM10"],df["PM25"],df["IDEX_NM"])
df=df[["MSRRGN_NM","MSRSTE_NM","PM10","PM25","IDEX_NM"]]
print(df)
#필드명 수정
df=df.rename(columns={"MSRRGN_NM":"권역","MSRSTE_NM":"구","PM10":"미세","PM25":"초미세","IDEX_NM":"상태"})
print(df)
#구 이름으로만 찾게
df=df.set_index(df["구"])
#종로구만
print(df.loc["종로구"])
#필드끼리 계산
df["합계"]=df["미세"]+df["초미세"]
#종로구->학원
df["구"]=df["구"].replace("종로구","학원")
#합계 내림차순 정렬
df=df.sort_values(by="합계",ascending=False)
print(df)
#가장 미세먼지 합계가 많은 구
print(df[df["합계"]==df["합계"].max()]["구"])
