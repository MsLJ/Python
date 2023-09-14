# -*- coding:utf-8 -*-
import pandas as pd
df=pd.read_csv("C:/lee/iscs.csv",names=["이름","업종","주소","항목","가격"])
print(df)
print("---------")
#업종별 평균가
#0원인거 삭제하고
df=df[df["가격"]>0]
# (df.groupby("종류")["가격"].mean()
print(df.groupby("업종")["가격"].mean())
#항목별 평균가
print(df.groupby("항목")["가격"].mean())

#구별 평균ㄴ가
# df["Name"]=df["Name"].apply(lambda n:n.split(",")[0])
print(df[df['주소'].isnull()])
df['주소']=df['주소'].fillna("서울특별시 모름")
#시리즈 타입에는 stratswith메소드가 없음
#endswith도 없고 그러니함수를 만들어서
def getGu(a):
    a=a.split(" ")
    if a[0].endswith("구"):
        return a[0]
    return a[1]
df["구"]=df["주소"].apply(getGu)
print(df.groupby("구")["가격"].mean())

    
#구별->업ㅂ종별 평균가
print(df.groupby(["구","업종"])["가격"].mean())




