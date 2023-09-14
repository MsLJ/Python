# -*- coding:utf-8 -*-
from idlelib.iomenu import encoding
from pymongo.mongo_client import MongoClient


f=open("C:/lee/DaumNews/DaumNews.txt","a",encoding="utf-8")
con=MongoClient("195.168.9.65")
db=con.xe
for n in db.daumNews.find():
    f.write(n["d_news"]+"\n")
    
con.close()
f.close()





