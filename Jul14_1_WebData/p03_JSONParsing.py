# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads

# JSON:데이터를 JavaScript에서 객체+배열 표현하는 방식으로
#[]: JS의 배열/Python list
#{}: JS의 객체/Python dict    
#openweathermap HTTP 통신 콘솔
#https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr


#l=["aa","bb","cc"]
#l[0]
#l[1]
#for v in l:
    #v사용
#######################
# d={"aa":1,"bb":2}
#d["aa"]
#d["bb"]

huc=HTTPSConnection("api.openweathermap.org")
huc.request("GET","/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = huc.getresponse().read()
print(resBody.decode())
############################################################
weatherData=loads(resBody)#Json -> python컬렉션
#날씨
#기온
#습도
#print(type(weatherData))
print(weatherData["weather"][0]["description"])
print(weatherData["main"]["temp"])
print(weatherData["main"]["humidity"])
    

huc.close()






























