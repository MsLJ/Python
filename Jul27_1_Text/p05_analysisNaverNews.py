# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from konlpy.tag._okt import Okt
from hanspell.spell_checker import check
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import requests
fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)
#MongoDB에 있는 네이버뉴스 다
con=MongoClient("195.168.9.65")
db=con.xe
o=Okt()
wc={}
for n in db.Naver_News.find():
    n=n["title"]+" "+n["description"]
    n=check(n).checked#맞춤법 교정
    n=o.normalize(n)#정규화
    #동사 원형 단어수 세기
    for w,p in o.pos(n,stem=True):#형태소 분석(동사원형으로)
        if p=="Verb":#동사만
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
wc2=[]
for w,c in wc.items():
    wc2.append({"단어":w,"횟수":c})
    
    
wcDF=pd.DataFrame(wc2)
wcDF=wcDF.sort_values(by="단어")
# print(wcDF)
wcDFtop20=wcDF.head(20)
sns.barplot(data=wcDFtop20,x="단어",y="횟수",palette="summer")
plt.show()
con.close()


















