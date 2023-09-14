# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads
from _datetime import datetime

y = input("년:")
f = open("C:/lee/busData" + y + ".csv", "a", encoding="utf-8")

huc = HTTPConnection("openapi.seoul.go.kr:8088")

for m in range(1, 13):
    for d in range(1, 32):
        for start in range(1,40002,1000):
            
            end=start+999
            dataRange="%d/%d"%(start,end)
            when = "%s%02d%02d" % (y, m, d)
            huc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/"+dataRange+"/"+ when)
            try:
            #if문을 써도 될것이다 
            #if"CardBusStatisticsServiceNew" in busdata:
                resBody = huc.getresponse().read()
                busdata = loads(resBody)
                for b in busdata["CardBusStatisticsServiceNew"]["row"]:
                    useDt = b["USE_DT"]
                    f.write("%s,%s,%s" % (useDt[0:4], useDt[4:6], useDt[6:8]))
                    f.write("," + b["BUS_ROUTE_NM"])
                    f.write("," + b["BUS_STA_NM"])
                    f.write((",%.0d") % (b["RIDE_PASGR_NUM"]))
                    f.write((",%.0d\n") % (b["ALIGHT_PASGR_NUM"]))
    
            except Exception as e:
                continue

f.close()
huc.close()
