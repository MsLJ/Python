# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

#데이터 없
#kaggle:분석 경진대회 샘플데이터
#타이타닉
#csv파일(첫줄에 제목 있는)로
#따로 f=뭐 작업할필요없이 그냥 pd.read(파일경로)적으면 알아서
#데이터 프레임으로 만들어줌
a=pd.read_csv("C:/lee/work space/titanic.csv")
print(a) 
print("---------")

#CSV파일(첫줄에 제목 없는)
#제목이 없으면 naems[]를 만들어 그안에 담아주면 알아서 해주는
b=pd.read_csv("C:/lee/subway/subway.csv",names=["년","월","일","노선","역"])
print(b)
print("----------")

#쟁여왔던 카카오 블로그  파일로
#어쨋든 파일
#.csv,.txt:확장자-MS Windows에만 있는 허상
#sep=구분자 탭키로 구분해놨으니
#비정형 데이터라 pandas가 안어울리는데 일단은 그냥 예제니까..
c=pd.read_csv("C:/lee/KakaoBlog.txt",sep="\t",names=["제목","내용","블로그명"])
print(c)
print("--------")

#OracleDB에 있는거
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select*from weather_Data"
d=pd.read_sql(sql,con)
print(d)

sql="select sm_MSRRGN_NM,avg(sm_PM10) "
sql+="from seoul_misaemungi "
sql+="group by sm_MSRRGN_NM "
e=pd.read_sql(sql,con)
print(e)
con.close()

#정형데이터
#     OracleDB에 :DB에서 SQL로 처리
#     CSV파일:Hadoop으로 처리
#비정형 데이터
#    데이터프레임은 좀 아니고
#    ->Pandas?













