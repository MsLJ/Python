# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용

df=pd.read_csv("C:/lee/cspf.csv",names=["월","노선","역","내고탐","그냥탐","내고내림","그냥내림"])
print(df)
df2=df.groupby("노선")[["내고탐","그냥탐","내고내림","그냥내림"]].mean()
print(df2)
no=df2.index
no2=np.arange(len(no))
prn=df2["내고탐"]
frn=df2["그냥탐"]
pan=df2["내고내림"]
fan=df2["그냥내림"]
plt.bar(no2-0.4,prn,width=0.4,align="edge",color="red")
plt.bar(no2-0.4,pan,width=0.4,align="edge",color="blue",bottom=prn)
plt.bar(no2,frn,width=0.4,align="edge",color="green")
plt.bar(no2,fan,width=0.4,align="edge",color="purple",bottom=frn)
plt.xticks(no2,no,rotation=45)
plt.legend(["내고탐","내고내림","그냥탐","그냥내림"])
plt.title("지하철")
plt.show()

