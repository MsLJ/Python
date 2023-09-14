# -*- coding:utf-8 -*-
import pandas as pd

df=pd.read_csv("C:/lee/kfoodPrice.csv",names=["어디","뭐","수량","가격","시장이름","지역"])
print("----------")

#시장이름으로찾게
df= df.set_index(df["시장이름"])
# df=df.sort_values(by="시장이름")
print(df)
print("----------")
#시장이름 가나다순으로 정렬
df= df.sort_index()
print(df)
print("----------")
#통인시장것만
df= df.set_index(df["어디"])
print(df.loc["통인시장"])
print("----------")
#농협시리즈만
print(df[df["어디"].str.contains("농협")])
print("-------")

#노원구에서 뭐뭐파나
print(df[df["지역"]=="노원구"]["뭐"])
print("-------")
#가격이 5만원이상
# print(df[df["가격"]>=50000])
# print("-------")
#가격 내림차순 ->품명 오름차순
df=df.sort_values(by=["가격","뭐"],ascending=[False,True])
print(df)