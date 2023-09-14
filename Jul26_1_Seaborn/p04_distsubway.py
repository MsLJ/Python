# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect
from http.client import HTTPConnection
from json import loads
from _datetime import datetime


fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

#지하철
df=pd.read_csv("C:/lee/subway/subway.csv",names=["년","월","일","호선","역","탄사람","내린사람"])

df["이용객수"]=df["탄사람"]+df["내린사람"]
#노선별 이용객수 분포
# sns.violinplot(data=df,x="호선",y="이용객수",palette="summer")
# plt.show()
#요일별 이용객수 분포
def getyoil(s):
    d="%d%02d%02d"%(s["년"],s["월"],s["일"])
    #date로 바꿔야 요일로 받을수있으니까
    d=datetime.strptime(d,"%Y%m%d")
    return datetime.strftime(d,"%A")
df["요일"]=df.apply(getyoil,axis=1)
sns.violinplot(data=df,x="요일",y="이용객수",palette="Spectral")
plt.show()





