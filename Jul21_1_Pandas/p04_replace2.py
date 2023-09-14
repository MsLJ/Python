# -*- coding:utf-8 -*-
import pandas as pd
df=pd.read_csv("C:/lee/work space/titanic.csv")
print(df.columns)

#타이타닉
#이름,성별 필드 빼고 다 지우고 Name Sex
df=df[["Name","Sex"]]
print(df)
#male->남자 ,female->여자
df["Sex"]=df["Sex"].replace({"male":"남자","female":"여자"})
#이름에서 mr->미스터


# df["Name"]=df["Name"].replace("Mr","미스터")
#이름에서 Mr->미스터
def replaceMr(t):
    return t.replace("Mr","미스터")
df["Name"]=df["Name"].apply(replaceMr)
print(df)
#이름에서 성때고 이름만 남기기
# def removeFamilyname(n):
#     return n.split(",")[0]
df["Name"]=df["Name"].apply(lambda n:n.split(",")[0])
print(df)
#def getHab(a,b):
#    return a+b
#c=  getHab(10,20)
c=(lambda a,b:a+b)(10,20)
print(c)
df=pd.read_csv("C:/lee/work space/titanic.csv")
print(df[df["Age"].isnull()])
#10대
#20대
#30대
#40대
#모름
#나이별대로 산사람/죽은사람 수
# def getDae(a):
#     return "%d0대"%(a//10)

df["Age"]=df["Age"].fillna(900)
print(df["Age"])
df["대"]=df["Age"].apply(lambda a:"%d0대"%(a//10))
df["대"]=df["대"].replace("900대","모름")
df["대"]=df["대"].replace("00대","0대")
print(df.groupby(["대","Survived"])["PassengerId"].count())

