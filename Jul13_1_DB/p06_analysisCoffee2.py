# -*- coding:utf-8 -*-
from cx_Oracle import connect

# OracleDB서버
#    CPU/RAM/HDD좋음
# PC
#    CPU/RAM/HDD부족

#Numpy:좋은 list
#Pandas:엑셀 느낌...


# OracleDB서버에 있는 100TB데이터를 인터넷으로 받아와서?(시간+용량+사양문제)
# PC에 csv?

#PC에 100TB짜리 csv파일
#list에??
#PC의 cpu로 계산?
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
#Oracle DB서버의 강력한 cpu로 계산

# 1)평균가
sql="select avg(c_price)from jul13_coffee"
cur=con.cursor()
cur.execute(sql)
for p in cur:
    print(int(p[0]))

cur.close()

# 2)메뉴 총 몇 종류
sql="SELECT COUNT(*)FROM jul13_coffee"
cur=con.cursor()
cur.execute(sql)
for p in cur:
    print(p[0])
cur.close()


# 3)최고가 메뉴 뭐
sql="SELECT * FROM JUL13_COFFEE WHERE C_PRICE = (SELECT MAX(C_PRICE) FROM JUL13_COFFEE)"
cur=con.cursor()
cur.execute(sql)
for mx in cur:
    print(mx)
cur.close()
#4)최저가
sql="SELECT * FROM jul13_coffee WHERE c_price=(SELECT min(c_price) FROM JUL13_COFFEE )"
cur=con.cursor()
cur.execute(sql)
for mm in cur:
    print(mm)
    
cur.close()



#5)카테고리별 평균가
#group by를  쓰면될것 
sql="SELECT c_cate,avg(c_price) FROM JUL13_COFFEE group BY c_cate"
cur=con.cursor()
cur.execute(sql)
for cate,price in cur:
    print(cate,price)


















con.close()



