# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.cluster._kmeans import KMeans
fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)
df=pd.read_csv("C:/lee/subway/subway.csv",names=["년","월","일","노선","역","승차","하차"])

trainData=df.to_numpy()
km=KMeans(10)
df["그룹"]=km.fit_predict(trainData)
print(df)

# sns.scatterplot(x="승차",y="하차",hue="그룹",data=df,palette="pastel")
# plt.show()
print("-------")
#역명-> 그룹 역 출력
name=input("역명:")
print(df.loc[name]["그룹"])
print(df[df["그룹"]=df.loc[name]["그룹"]])