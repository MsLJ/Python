# -*- coding:utf-8 -*-
from cx_Oracle import connect

#DB에 저장돼어있는 커피데이터를 csv파일로 옮겨

ff=open("C:/lee/0713.csv","a",encoding="utf-8")


con = connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql = "select * from jul13_coffee" 

cur = con.cursor()
cur.execute(sql)

for name,cate,price in cur:
    data=("%s,%s,%d\n")%(name,cate,price)
    ff.write(data)
  

ff.close()
cur.close()
con.close()

