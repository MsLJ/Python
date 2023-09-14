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

f=(frn+fan)/2
f=f/f.max()*1000
print(f)
#돈내고 ㅏㅁㄶ이 타면,돈내고 많이내림
#근데 그거랑 무임시리즈 무관
plt.scatter(prn,pan,s=f,color="green",alpha=0.5)
plt.title("지하철")
plt.show()
