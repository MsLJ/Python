# -*- coding:utf-8 -*-
from cx_Oracle import connect


f=open("C:/lee/weather+misae/weahterData.csv", "a", encoding="utf-8")
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
cur = con.cursor()

sql="select * from weather_data order by w_date"
cur.execute(sql)  
for d,dsc,tm,hm in cur:
    data=("%d,%d,%d,%d,%s,%.2f,%d")%(d.year,d.month,d.day,d.hour,dsc,tm,hm)
    f.write(data+"\n")
f.close()
con.close()













