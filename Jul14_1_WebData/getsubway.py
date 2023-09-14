# -*- coding:utf-8 -*-
#http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/5/20151101
from http.client import HTTPConnection
from _datetime import date
from xml.etree.ElementTree import fromstring
#2015,1,1,1호선,서울역,10000,20000
#기존에 만들었던것들은 다 실시간데이터이기에 DB에 저장해서 담아둘만했던
#->오늘날짜가 아니면 더이상 구할수가없는... 날짜가 지나면
#하지만 이번에 하는건 실시간이 아닌 예전의 데이터 그 날짜를 입력하면 그 날짜의 데이터를 받아오는
#그렇기에 -> 바로 CSV파일로
f=open("C:/lee/subway/subway.csv", "a", encoding="utf-8")
huc = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(2015,2023):
    for m in range(1,13):
        for d in range(1,32): 
            when="%d%02d%02d"%(y,m,d)
            huc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/610/"+when)
            resBody = huc.getresponse().read()
            #print(resBody.decode())
            for sub in fromstring(resBody).getiterator("row"):
                useDt=sub.find("USE_DT").text
                f.write("%s,%s,%s"%(useDt[0:4],useDt[4:6],useDt[6:8]))
                f.write(","+sub.find("LINE_NUM").text)
                f.write(","+sub.find("SUB_STA_NM").text)
                f.write(","+sub.find("RIDE_PASGR_NUM").text)
                f.write(","+sub.find("ALIGHT_PASGR_NUM").text+"\n")
            print(when)
  

huc.close()
f.close()






































