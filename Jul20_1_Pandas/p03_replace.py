# -*- coding:utf-8 -*-
import pandas as pd

#원본 수정을 안하려고-->~~작업해서 새 df만들기
df=pd.read_csv("C:/lee/kfoodPrice.csv",names=["어디","뭐","종류","가격","물건파는곳","지역"])
print(df)
print("----------")

#전통시장->장터
df=df.replace("전통시장","장터")
print(df)
print("----------")
#특정필드
#대형마트->mart
df["종류"]=df["종류"].replace("대형마트","mart")
print(df)
print("---------")

#한꺼번에 여러개 수정
#장터->전통시장,mart->대형마트
# df["종류"]=df['종류'].replace(["장터","mart"],["전통시장","대형마트"])
# print(df)
# print("--------------")

#한꺼번에 여러개 수정
#전통시장 ->일요일에 함,대형마트->일요일에 쉼
df["종류"]=df['종류'].replace({"전통시장":"함","대형마트":"안함"})
print(df)
print("------------")

#한꺼번에 여러개 수정
#함/안함->물건파는곳
df["종류"]=df['종류'].replace(["함","안함"],"물건파는곳")
print(df)

#필드명수정
df=df.rename(columns={"어디":"이름","뭐":"물품"})
print(df)