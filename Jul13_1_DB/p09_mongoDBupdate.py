# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

#MongoDB:NoSQL->JavaScript로
#    JavaScript 나  Python나 문법이
#    테이블 ->JS배열:[1,2,3]:Python List
#    데이터 ->JS객체:{}:Python dict


con=MongoClient("195.168.9.65")
db=con.xe#con.db명


n=input("이름:")
c=input("카테고리:")
p=int(input("가격:"))
#Python dict (JS객체랑 생긴게 같음)
w={"name":n}
s={"$set":{"price":p}}
#MongoDB랑 문법 거의 비슷
#result=db.jul13_coffee.update_many(찾,바)
result=db.jul13_coffee.update_many(w,s)

#help(result)
if result.modified_count>=1:
    print("성공")








con.close()










