# -*- coding:utf-8 -*-
from cx_Oracle import connect


#DB에 저장된 기상청 날씨 예보 데이터
#csv로 저장하는 프로그램

#년,월,일,시,기온,날씨
#2023,07,13,21,20.0,비

f = open("C:/lee/kmaweahter.csv", "a", encoding="utf-8")
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select*from kma_weather order by kw_date,kw_hour"
cur = con.cursor()
cur.execute(sql)
for day,hour,temp,wfkor in cur:
    #print(datetime.strftime(d,"%y,%m,%d"))
    data=("%s,%s,%s,%.00f,%.1f,%s\n")%(day.year,day.month,day.day,hour,temp,wfkor)
    f.write(data)


f.close()
cur.close()
con.close()