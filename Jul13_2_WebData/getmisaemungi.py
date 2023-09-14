# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect
from _datetime import date

#실시간
#서울시 권역별 실시간 대기환경 현황을
#내 DB에 저장하는 Red
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
#http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/
huc=HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
resBody=huc.getresponse().read()
#print(resBody)
#mungis=fromstring(resBody).getiterator("row")

cur = con.cursor()
for m in fromstring(resBody).getiterator("row"):
    q=m.find("MSRRGN_NM").text
    w=m.find("MSRSTE_NM").text
    e=int(m.find("PM10").text)
    r=int(m.find("PM25").text)
    t=m.find("IDEX_NM").text
    sql = "insert into seoul_misaemungi" 
    sql += " values(sysdate,'%s','%s',%f,%f,'%s')" % (q,w,e,r,t)
    cur.execute(sql)    

con.commit()
cur.close()
con.close()
    
huc.close()












