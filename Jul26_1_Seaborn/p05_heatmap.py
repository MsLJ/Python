# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect
from json import loads
from _datetime import datetime


fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

#지하철
df=pd.read_csv("C:/lee/subway/subway.csv",names=["년","월","일","호선","역","탄사람","내린사람"])
df["이용객수"]=df["탄사람"]+df["내린사람"]

#피벗테이블(테이블을 요약해놓은 테이블)
#월별 이용객수 를 노선으로 찾도록
pt=df.pivot_table(columns="월",values="이용객수",index="호선")
print(pt)




sns.heatmap(data=pt,camp="summer")
plt.show()





