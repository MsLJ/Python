# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용
yData=[10,20,30,40,2]
xData=["s","a","d","b","t"]

#기본
# plt.bar(xData,yData)
# plt.show()

#디자인
# plt.bar(xData,yData,color="red",width=0.5,edgecolor="orange",linewidth=3)
# cs=["red","orange","yellow","green","blue"]
# plt.bar(xData,yData,color="red",width=0.5,edgecolor="orange",linewidth=3)
# plt.show()

#여러개
# yData2=[12,33,53,1,23]
# xData2=np.arange(len(yData2))#0 1 2 3 4
# xData3=xData2-0.4#-0.4 0.6 ...
# # plt.bar(xData,yData,align="edge")
# plt.bar(xData3,yData,width=0.4,align="edge")
# plt.bar(xData,yData2,width=0.4,align="edge",color="green")
# plt.show()

#여러개(위에 -누적합)
yData2=[12,33,53,1,23]
plt.bar(xData,yData,color="red")
plt.bar(xData,yData2,color="blue",bottom=yData)
plt.show()


