# -*- coding:utf-8 -*-
#서울시 모기예보제 정보
#2016.5.1~2016.10.31
#..
#어제까지
#csv로
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/MosquitoStatus/1/5/2020-04-12
import pandas as pd
import numpy as np
#물가/집/공원 평균치
#모기가 가장 심했던날
df=pd.read_csv("C:/lee/mosquitos.csv",names=["날짜","물가","집","공원"])
print(df)
#csv는 글자로 인식-x

#지금 다 글자인상태라 나누기가 안돼는 상태
# df["종류"]=df["종류"].replace("대형마트","mart")
# df["물가"]=df["물가"].replace("None","0")
# df["집"]=df["집"].replace("None","0")
# df["공원"]=df["공원"].replace("None","0")
#내가 한 방식은 어차피 평균 구할꺼니까 0으로 바꿨고
df=df.replace("None",0)
df=df.astype({'물가':'float', '집':'float','공원':'float'})
# df=df["물가"].astype('float')
# df=df["집"].astype('float')
# df=df["공원"].astype('float')

#*수업때 진행한 방식= 그냥 None을 다 없애자 넘파이 np.nan을 사용해서*
df["물가"]=df["물가"].replace("None",np.nan)
df["집"]=df["집"].replace("None",np.nan)
df["공원"]=df["공원"].replace("None",np.nan)

df["물가"]=pd.to_numeric(df['물가'])
df["집"]=pd.to_numeric(df['집'])
df["공원"]=pd.to_numeric(df['공원'])

#필드 형변환 (글자로)
#df['물가']=df['물가'].astype(str)

# print(type(df["물가"]))#시리즈 타입
# print(df["물가"].dtype)#자료형 타입 보기.dtype

#없는거는 평균치로 채워서
df["물가"]=df['물가'].fillna(df['물가'].mean())
df["집"]=df["집"].fillna(df['집'].mean())
df["공원"]=df["공원"].fillna(df['공원'].mean())



#물가/집/공원 평균치
df["평균"]=(df["물가"]+df["집"]+df["공원"])/3
print(df["평균"])



#모기가 가장 심했던날 언제
print(df[df['평균']==df['평균'].max()])



