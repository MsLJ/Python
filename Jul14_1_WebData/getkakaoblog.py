from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads
from pymongo.mongo_client import MongoClient


#https://dapi.kakao.com/v2/search/blog
#Authorization: KakaoAK ${REST_API_KEY}
#b8fa6b88c1acddea8f6e06afb295981b
def clean(s):
    s = s.replace("&apos;", "").replace("&amp;", "")
    s = s.replace("<b>", "").replace("</b>", "")
    s = s.replace("&quot;","")
    return s
#########################################################
query="맛집"
query=quote(query)
#h={"헤더명":"값"}
h = {"Authorization":"KakaoAK b8fa6b88c1acddea8f6e06afb295981b"}
huc=HTTPSConnection("dapi.kakao.com")
huc.request("GET","/v2/search/blog?query="+query,headers=h)

con=MongoClient("195.168.9.65")
db=con.xe

resBody = huc.getresponse().read()
#print(resBody.decode())
blog=loads(resBody)
for b in blog["documents"]:
  
    data={"title":clean(b["title"]),"contents":clean(b["contents"]),"blogname":clean(b["blogname"])}
    db.KakaoBlog.insert_one(data)
   
    
    
con.close() 
huc.close()
    
    
 





