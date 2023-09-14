# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
#서울시 모기예보제 정보
#2016.5.1~2016.10.31
#..
#어제까지
#csv로
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/MosquitoStatus/1/5/2020-04-12
f=open("C:/lee/mosquitos.csv", "a",encoding="utf-8")
huc=HTTPConnection("openapi.seoul.go.kr:8088")
for y in range(2016,2024):
    for m in range(5,11):
        for d in range(1,32):
            when = "%d-%02d-%02d" % (y, m, d)
    
            huc.request("GET","/575a4655496b636839386f58586542/xml/MosquitoStatus/1/1/"+when)
            resBody=huc.getresponse().read()
            mosquitos=fromstring(resBody).getiterator("row")
            for v in mosquitos:
                data=("%s,%s,%s,%s\n")%(v.find("MOSQUITO_DATE").text,v.find("MOSQUITO_VALUE_WATER").text,v.find("MOSQUITO_VALUE_HOUSE").text,v.find("MOSQUITO_VALUE_PARK").text)
            #     print(v.find("MOSQUITO_DATE").text)
            #     print(v.find("MOSQUITO_VALUE_WATER").text)
            #     print(v.find("MOSQUITO_VALUE_HOUSE").text)
            #     print(v.find("MOSQUITO_VALUE_PARK").text)
                f.write(data)
f.close()
huc.close()














