# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
from cx_Oracle import connect



huc=HTTPSConnection("api.openweathermap.org")
huc.request("GET","/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = huc.getresponse().read()
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
cur = con.cursor()

#print(resBody.decode())
weatherData=loads(resBody)
dcs=weatherData["weather"][0]["description"]
tmp=weatherData["main"]["temp"]
hdt=weatherData["main"]["humidity"]
sql="insert into weather_Data values(sysdate,'%s',%.2f,%d)"%(dcs,tmp,hdt)
cur.execute(sql)     
con.commit()
cur.close()
con.close()
huc.close()












