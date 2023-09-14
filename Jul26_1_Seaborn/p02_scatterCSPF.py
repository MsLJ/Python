# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect


fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

#지하철 내고타고,...
df=pd.read_csv("C:/lee/cspf.csv",names=["월","노선","역","내고탐","그냥탐","내고내림","그냥내림"])
print(df)

#내고타,그냥타 관계
# sns.scatterplot(x="내고탐",y="그냥탐",data=df)
# plt.show()
#내고타,그녕타 관계 노선별 다른색
# sns.scatterplot(x="내고탐",y="그냥탐",data=df,hue="노선",palette="Accent")
# plt.show()
#내고타,내고내려 관계
# sns.scatterplot(x="내고탐",y="내고내림",data=df,hue="노선",palette="Accent")
# plt.show()

#내고타 내고내려 관계(그냥타+그냥내려로)크기
df["그냥합"]=df["그냥탐"]+df["그냥내림"]
sns.scatterplot(data=df,x="내고탐",y="내고내림",size="그냥합",palette="Accent")
plt.show()

