# -*- coding:utf-8 -*-

# AI분야
#     Machine Learning
#               문제를 해결하는데 필요한 알고리즘을 사람이 지정해주는거
#                비만도 검사 , 가위바위보,....
#                좀 AI스러운 알고리즘 몇개 소개
#     Deep Learning
#    지도학습:인간들이 결과를 구해놓은거를 AI한테 학습
#

#               문제를 해결하는데 필요한 알고리즘도 컴이 찾아내서
#                인공신경망 구성해서...



#AI 라이브러리가 없어서
# 그 알고리즘 만들려면:수학/수학적 사고력 필요
#
###########################################################
#scikit-learn:머신러닝 라이브러리
#pip install sklearn
#pip3.6 install wheel
#pip3.6 install -U scikit-learn
#
#kNN(k-Nearest Neighbor)알고리즘
#    사람들은 분류할때 비슷한거 기준으로
#    학습데이터들을 그래프 상의 점으로 놓고 
#    예측해봐야하는 데이터와 가장 가까운 k를 찾아서 
#    다수결로 결론

import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier

trainData=np.array([[80,20],[95,5],[10,90],[5,95],[30,50]])
label=np.array(["액션","액션","조폭","액션","조폭"])

knc=KNeighborsClassifier(3)#가장 가까운 3개를 뽑아서
knc.fit(trainData,label)#학습시키기

x=float(input("격투씬 비율:"))
y=float(input("욕씬 비율:"))
xy=np.array([[x,y]])
result=knc.predict(xy)#에측시키기
print(result)














