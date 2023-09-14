# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

#이건 제목에 , 이런식으로 한후에 내용이 이어지는것이기에
#CSV파일에 넣게된다면 추후에 다시 이 데이터를 가져와서 사용할려고할때
#불편함이 있을것 그러니까 그냥 TXT에다가 저장을 하자
con=MongoClient("195.168.9.65")
db=con.xe#con.db명
f = open("C:/lee/work space/Project/TRACENEWSHAB.txt", "a", encoding="utf-8")

result=db.Trace_News_world.find()
for n in result:
    f.write("%s"%n["title"])
    f.write(n["description"].replace("&quot;", ""))


print("끝")
f.close()
con.close()