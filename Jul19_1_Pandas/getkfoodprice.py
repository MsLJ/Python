# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/ListNecessariesPricesService/1/5/
#여기서도 똑같이 한번에 데이터를 1000개씩 밖에 못받으니까
#저번에 했던것처럼 for문 돌려서
f=open("C:/lee/kfoodPrice.csv","a",encoding="utf-8")
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for i in range(1,558631,1000):
    #t="%d,%d"%(i,i+999) 이렇게 하는게 더 깔끔할거같다
    ii=i+999
    huc.request("GET", "/575a4655496b636839386f58586542/json/ListNecessariesPricesService/%d/%d"%(i,ii))
    try:
        resBody = huc.getresponse().read()
        # print(resBody.decode())
        kfoodPrice=loads(resBody)
        #print(kfoodPrice)
        for l in kfoodPrice["ListNecessariesPricesService"]["row"]:
            data=("%s,%s,%s,%s,%s\n")%(l["M_NAME"].replace(",","."),l["A_NAME"].replace(",","."),l["A_PRICE"].replace(",","."),l["M_TYPE_NAME"].replace(",","."),l["M_GU_NAME"].replace(",","."))
            f.write(data)
    #     print(l["M_NAME"])
    #     print(l["A_NAME"])
    #     print(l["A_PRICE"])
    #     print(l["M_TYPE_NAME"])
    #     print(l["M_GU_NAME"])
    except Exception as e:
        continue




f.close()
huc.close()
