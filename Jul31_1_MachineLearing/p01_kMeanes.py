# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.cluster._kmeans import KMeans
from sklearn.neighbors._classification import KNeighborsClassifier
from idlelib.pyshell import PORT
fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)



#KMeans:k개의 평균
#    비지도학습
#    주어진 데이터들을 비슷한것끼리 군집화(clustering)


#    데이터들을 그래프상에 점 찍고(빨간)
#    k개의 랜덤한 점 찍고(초록)
#    초록-빨강 거리 구해서 가까운것 끼리 군집화 
#    그 군집 내에서 평균 구해서 k개의 초록 점 다시
#    초록-빨강 거리 구해서 가까운것 끼리 군집화 
#    그 군집 내에서 평균 구해서 k개의 초록 점 다시
#    초록-빨강 거리 구해서 가까운것 끼리 군집화 
#    초록 점이 더이상 안움직일때까지 반복
#    끝나면 그 군집을 최종적으로 결과로 내는


#seaborn으로 
df=pd.DataFrame()
df["싸움"]=[80,20,95,5,10]
df["욕"]=[90,5,95,30,50]
print(df)
print("------")
traiData=df.to_numpy()
print(traiData)

#머신러닝 알고리즘 직접 구현하자
#머신러닝 라이브러리 쓰자
km=KMeans(3)
df["그룹"]=km.fit_predict(traiData)
print(df)

# sns.scatterplot(x="싸움",y="욕",hue="그륩",data=df,palette="pastel")
#plt.show()

#kMeans로 라벨링 +kNN으로 예측
label=df["그룹"].to_numpy()
knc=KNeighborsClassifier(3)
knc.fit(traiData, label)
a=float(input("싸움:"))
b=float(input("욕:"))
predictData=np.array([[a,b]])

result=knc.predict(predictData)[0]
print(result)







