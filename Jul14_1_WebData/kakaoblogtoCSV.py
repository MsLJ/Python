# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient


con=MongoClient("195.168.9.65")
db=con.xe
f = open("C:/lee/KakaoBlog.txt", "a", encoding="utf-8")

result=db.KakaoBlog.find()
for k in result:
    data=("%s\t%s\t%s\t")%(k["title"],k["contents"],k["blogname"])
    f.write(data+"\n")


f.close()
con.close()