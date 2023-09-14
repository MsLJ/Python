# -*- coding:utf-8 -*-
from cx_Oracle import connect

# 연결
con = connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")

sql = "select * from jul13_coffee" 
print(sql)

# DB관련 작업 총괄매니져 (PreparedStatement)겸 결과(ResultSet)
cur = con.cursor()
# SQL을 서버로 전송,실행
# 결과가 cur에 저장
cur.execute(sql)

for name,cate,price in cur:
    #그리고 tuple 특성상 값을 하나에 받는게 아닌 여러개로 받을수있는
    print(name)
    print(cate)
    print(price)
    print("---------")
#for c in cur:
#     print(c,type(c))
#     #tuple이 어차피 컬렉션이기에 가능한
#     print(c[0])
#     print(c[1])
#     print(c[2])
#     print("---------")
   



cur.close()
con.close()

