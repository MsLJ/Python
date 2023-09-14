# -*- coding:utf-8 -*-
from cx_Oracle import connect

# J: JDBC-> ConnectionPool->MyBatis
# P:
# 연결
con = connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")

# 데이터 확보
n = input("이름:")
c= input("카테고리:")
p = int(input("가격:"))

# SQL(완성,;빼고)
sql = "insert into jul13_coffee" 
sql += " values('%s','%s',%d)" % (n,c, p)
print(sql)

# DB관련 작업 총괄매니져 (PreparedStatement)
# 겸 결과
cur = con.cursor()
print(type(cur))

# SQL을 서버로 전송,실행
# 결과가 cur에 저장
cur.execute(sql)

if cur.rowcount==1:
    print("성공")
    #여기도 commit해줘야 반영
    con.commit()


cur.close()
con.close()

