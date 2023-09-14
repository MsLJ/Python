# -*- coding:utf-8 -*-
# https://news.daum.net/
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

# 로그인해야 하면?
# JS로 동적으로 추가되는거면?
# 웹 브라우저 접근만 허용,프로그램으로 요청 막았으면?
# ->셀레늄 (웹 브라우저 매크로)
def clean(s):
    s = s.replace("&apos;", "").replace("&amp;", "")
    s = s.replace("<b>", "").replace("</b>", "")
    s = s.replace("&quot;", "")
    s = s.replace("\n", "")

    return s

con = MongoClient("195.168.9.65")
db = con.xe

huc = HTTPSConnection("news.daum.net")
huc.request("GET", "/")
resBody = huc.getresponse().read()
# print(resBody.decode())
daumNewsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")
# print(daumNewsData)
# 클레스니까 앞에 .
# cont_thumb
news = daumNewsData.select(".list_newsissue .link_txt")
for n in news:
    #strip()메서드를 사용하면될것 앞에 띄워쓰기 없애는건
    #print(n.text.strip())
    nt = n.text.strip()
    d = {"d_news":nt}
    result = db.daumNews.insert_one(d)
if result.acknowledged:
        print("성공")
        
        
        
con.close()
