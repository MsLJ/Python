# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

#http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/5/201501/

f=open("C:/lee/cspf.csv","a",encoding="utf-8")


for y in range(2015,2023):
    for m in range(1,13):
        t="%d%02d"%(y,m)
        huc=HTTPConnection("openapi.seoul.go.kr:8088")
        huc.request("GET","/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/700/"+t)
                
        rb=huc.getresponse().read()
        for i in loads(rb)["CardSubwayPayFree"]["row"]:
            f.write("%s,"% i["USE_MON"])
            f.write("%s,"%i["LINE_NUM"])
            f.write("%s,"%i["SUB_STA_NM"].replace(",","."))
            f.write("%.0f,"%i["PAY_RIDE_NUM"])
            f.write("%.0f,"%i["FREE_RIDE_NUM"])
            f.write("%.0f,"%i["PAY_ALIGHT_NUM"])
            f.write("%.0f\n"%i["FREE_ALIGHT_NUM"])
    
f.close()
huc.close()

