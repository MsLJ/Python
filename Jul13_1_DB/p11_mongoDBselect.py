# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con=MongoClient("195.168.9.65")
db=con.xe#con.db명


result=db.jul13_coffee.find()

for c in result :
    print(c)
    print(c["name"],c["price"],c["cate"])








con.close()










