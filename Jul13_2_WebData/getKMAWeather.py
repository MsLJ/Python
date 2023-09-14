# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect
from _datetime import date


#BD/AI 1단계: 분석용 데이터 구축
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")

huc=HTTPSConnection("www.kma.go.kr")
huc.request("GET","/wid/queryDFSRSS.jsp?zone=1168066000")
resBody=huc.getresponse().read()
weathers=fromstring(resBody).getiterator("data")#<data></data>들

                                    #$(kmaData).find("data")...
#pstmt : 자동 commit ->1회용
#cur:수동 commit->여러번
cur = con.cursor()
for w in fromstring(resBody).getiterator("data"):
    #1이 돼면 브레이크 하면될것 내가 생각한건 0일때 찾는거였는데
    if w.find("day").text=="1":
        break
    h=w.find("hour").text#<hour></hour>
    t=float(w.find("temp").text)
    wf=w.find("wfKor").text
        
    sql = "insert into kma_weather" 
    sql += " values(sysdate,'%s',%f,'%s')" % (h,t,wf)
    cur.execute(sql)

con.commit()
cur.close()
con.close()
    
huc.close()
    #print(type(w))












