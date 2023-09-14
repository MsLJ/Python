# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용

#지하철 csv불러서
df=pd.read_csv("C:/lee/subway/subway.csv",names=["년","월","일","호선","역","탄사람","내린사람"])

print(df)


df["이용객수"]=df["탄사람"]+df["내린사람"]
# bd=datetime.strptime(bd,"%Y/%m/%d")
# bda=datetime.strftime(bd,"%A")
# def test(t):
#     df["날짜"]=t["년"]+t["월"]+t["일"]
# df.apply(test,axis=1)

def getyoil(s):
    date="%d%02d%02d"%(s["년"],s["월"],s["일"])
    date=datetime.strptime(date,"%Y%m%d")
    return datetime.strftime(date,"%A")
#기존에 생각한건  그대로 판다스 형식으로 더하는건데 이렇게하면 타입이 부적절하다고 안됌
#함수 하나를 만들어서 거기서 계산을 하자

df["요일"]=df.apply(getyoil,axis=1)
# df["날짜"]=datetime.strptime(df["날짜"],"%Y%m%d")
# df["요일"]=datetime.strftime(df["날짜"],"%A")

#그래프
# sns.barplot(x="호선",y="이용객수",data=df)

#노선별 이용객수 평균
# sns.countplot(x="호선",data=df)



#노선별 이용객수 평균(요일별로 따로)
# sns.barplot(x="호선",y="이용객수",hue="요일",data=df)
# sns.countplot(x="요일",data=df)
plt.show()



