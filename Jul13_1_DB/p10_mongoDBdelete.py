# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

#MongoDB:NoSQL->JavaScript로
#    JavaScript 나  Python나 문법이
#    테이블 ->JS배열:[1,2,3]:Python List
#    데이터 ->JS객체:{}:Python dict


con=MongoClient("195.168.9.65")
db=con.xe#con.db명


n=input("이름:")
w={"name":{"$regex":n}}
result=db.jul13_coffee.delete_many(w)

if result.deleted_count>=1:
    print("성공")








con.close()










