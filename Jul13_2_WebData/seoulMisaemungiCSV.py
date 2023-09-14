# -*- coding:utf-8 -*-
from cx_Oracle import connect

#DB에 있는 미세먼지 데이터
#CSV로 만드는 Green

f = open("C:/lee/weather+misae/seoulMisaeMungi.csv", "a", encoding="utf-8")
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select*from SEOUL_MISAEMUNGI"
cur = con.cursor()
cur.execute(sql)
for day,q,w,pm10,pm25,idex in cur:
    #만약에 년도 월 일형식으로 자료를 넣고싶다면 datetime.strptime(day,"%Y/%m/%d")
    data=("%s,%s,%s,%s,%s,%d,%d,%s\n")%(day.year,day.month,day.day,q,w,pm10,pm25,idex)
    f.write(data)


f.close()
cur.close()
con.close()