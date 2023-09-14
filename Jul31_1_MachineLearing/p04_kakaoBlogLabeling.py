# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

#카카오블로그 글 출력
con=MongoClient("195.168.9.65")
db=con.xe

for b in db.KakaoBlog.find():
    print(b["blogname"]+"--------")
    print(b["title"])
    print(b["contents"])
    what=input("뭐:")
    db.KakaoBlog.update_one(
        {"_id":b["_id"]},
        {"$set":{"what":what}}
                            
                            )
    
con.close()
    