
# -*- coding:utf-8 -*-
import pandas as pd

#titanic
titanicDF=pd.read_csv("C:/lee/work space/titanic.csv")
print(titanicDF)
print("-----------")
print(titanicDF.shape)#몇행몇열
print("-----------")
print(titanicDF.columns)#필드명들
print("-----------")
print(titanicDF.head())#앞에서부터 몇개
print("-----------")
print(titanicDF.tail(2))#뒤에서부터 몇개
print("-----------")
print("열(필드) 기준=====")
print(titanicDF["Name"])#변수명["필드명"]
print("-----------")
print(titanicDF.Name)#변수명.필드명
print("-----------")
print(titanicDF[["Name","Age"]])#변수명[list형태로 필드명들]
print("행(데이터)기준==")
print(titanicDF.iloc[0])#0번 데이터:변수명.iloc[인덱스]
print("--------")
print(titanicDF.iloc[0:3])#0~(3-1)번 데이터
print("--------")
titanicDF=titanicDF.set_index(titanicDF["Name"])#찾는 기준 설정
print(titanicDF.loc["Behr, Mr. Karl Howell"])
print("---------")
print(titanicDF.iloc[1])#번호로
print("---------")
print(titanicDF.loc["Behr, Mr. Karl Howell"])#설정한 index로 찾기
print(titanicDF.loc["Behr, Mr. Karl Howell":"Graham, Miss. Margaret Edith"])#범위조회

print("열+행(데이터의 특정 필드) 조회====")
print(titanicDF.loc["Behr, Mr. Karl Howell"]["Age"])#변수명.loc[뭐][필드명]
print("-------")
print(titanicDF.loc["Behr, Mr. Karl Howell","Age"])#변수명.loc[뭐,필드명]
print("조건으로 조회=====")
print(titanicDF["Age"]>30)#True/False
print("---------")
#20대만
#20<=titanicDF["Age"] <=29
# titanicDF["Age"]>=20 and titanicDF["Age"]<=29
#        &&:중간에 생략되는 버전
#Numpy/Pandas에서는 중간에 생략되는 버전을 쓰면안돼니
#and->&
#or->|
print(titanicDF[(titanicDF["Age"]<30)&(titanicDF["Age"])>19])



