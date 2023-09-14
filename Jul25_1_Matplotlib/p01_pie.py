# -*- coding:utf-8 -*-

#삼국지연의:유비를 주인공으로...
#조조
#유비
#손권
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
#분석용 데이터 구축 : UTF-8인코딩으로

fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용


df=pd.read_csv("C:/lee/samReuslt.txt",sep="\t",names=["누구","몇번"])
df=df.sort_values(by="몇번",ascending=False)
print(df)
name=df['누구']
count=df['몇번']
#절대적인 크기 비교
# plt.bar(name,count)
# plt.show()

#비율
c=["red","green","blue"]
e=[0,0,0.2]
w={"edgecolor":"black","linewidth":3,"width":0.9}
plt.pie(count,labels=name,autopct="%.1f%%",colors=c,explode=e,startangle=45,wedgeprops=w)
plt.title("삼국지")
plt.show()

#ㅋㅌ단톡방 누가 말 많이하는지




