# -*- coding:utf-8 -*-
from http.client import HTTPSConnection

from xml.etree.ElementTree import fromstring
from urllib.parse import quote
from pymongo.mongo_client import MongoClient
from test.libregrtest.cmdline import DESCRIPTION
from _datetime import datetime

# 네이버 개발자 센터-> 뉴스 데이터 XML로

def clean(s):
    s = s.replace("&apos;", "").replace("&amp;", "")
    s = s.replace("<b>", "").replace("</b>", "")
    s = s.replace("&quot;","")
    s = s.replace("&lt;","").replace("&gt;","")
    return s

# https://openapi.naver.com/v1/search/news.xml
con=MongoClient("195.168.9.65")
db=con.xe#con.db명



huc = HTTPSConnection("openapi.naver.com")
query = "과학"  # 파이썬에서 quote()사용 urllib꺼
query = quote(query)
dsp=100;
dsp=str(dsp)
# 요청헤더
h = {"X-Naver-Client-Id":"js8a3iKcJsnzGvTy7N0Y",
   "X-Naver-Client-Secret":"lGgWGRmKYz"}
# 헤더는 그냥 주소 뒤에 headers
for start in range(1,1000,99):
    start=str(start)
    huc.request("GET", "/v1/search/news.xml?query=" + query+"&display="+dsp+"&start="+start,headers=h)
    resBody = huc.getresponse().read()
    #print(resBody.decode())
    news = fromstring(resBody).getiterator("item")





    for n in news:
        try:
            tt = clean(n.find("title").text)
            # text는 변수로 사용해야 하며 메소드가 아닙니다.
            # .text()가 아니라 .text
            dsc = clean(n.find("description").text)
            pbd=n.find("pubDate").text
            parsed_date = datetime.strptime(pbd, "%a, %d %b %Y %H:%M:%S %z")
            formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
            combined_datetime = parsed_date.replace(second=0, microsecond=0)
            l=n.find("link").text
            d = {"_id":l,"title": tt, "description": dsc,"pubdate":combined_datetime}
                
            result=db.Trace_News_it.insert_one(d)  
            
            if result.acknowledged:
                print("성공")
        except Exception as e:
            continue
    
huc.close()   
    
con.close()
