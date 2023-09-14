# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#matplotlib이 쓰는 기본폰트가 한글이 없어서
#한글이 되는 폰트로 바꿔야
#C:\windows\fonts에 가서 확인 cmd ->dir로 확인
#폰트이름x,폰트파일명
fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용
#Numpy/Pandas->sql
#matplotlib/
#pip install matplotlib

#numpy array를 대상
xData=np.array([10,20,30,40,50])
yData=[10,32,1,5,23]#list  -> numpy array로 자동으로 바꿔서

#기본
# plt.plot(yData)
# plt.show()

#x,y
# plt.plot(xData,yData)
# plt.show()


#축
# plt.plot(xData,yData)
# plt.xlabel("엑스축")
# plt.ylabel("yyyy")
# plt.axis([0,100,1,200])#x시작,x끝,y시작,y끝
# plt.show()

#제목
# plt.plot(xData,yData)
# # plt.title("제목")
# plt.title("제목",loc="left")#left,center,right
# plt.title("ㅋㅋㅋ",loc="right")#여러개가능
# d={"fontsize":20,"fontweight":"bold","color":"#FF0000"}
# plt.title("w",loc="center",fontdict=d)
# plt.show
# plt.show()

#선 (간단하게)
#matplotlib cheatsheet
# plt.plot(xData,yData,"m:P")#색,선,마커
# plt.show()
#선
# plt.plot(xData,yData,color="#43A047",linestyle="-.",marker="D",
#          linewidth=5,markersize=10)#색,선,마커
# plt.show()
#그리드
# plt.plot(xData,yData)
# plt.grid(axis="y",color="red",linestyle=":")
# plt.grid(axis="x")
# plt.show()

#눈금
# plt.plot(xData,yData)
# plt.xticks(xData, ["십","이십","삼십","사십","오십"])
# plt.yticks(yData, ["십","이십","삼십","사십","오십"])

#균등하게 하자면 그냥 하나더 만들기
# plt.yticks(np.arange(10,51,10), ["십","이십","삼십","사십","오십"])
#     #x,y,both         in, out, inout    눈금-글자 간격
# plt.tick_params("y",direction="inout",length=15,pad=30)
# plt.tick_params("x",labelsize=30,labelcolor="#0000FF")
# 
# plt.show()

# yData2=[100,300,10,50,30]
# plt.plot(xData,yData,color="red")
# plt.plot(xData,yData2,color="green")
# plt.legend(["빨강","녹색"])
# plt.show()

#y축을 여러개로 선 여러개
yData2=[100,300,100,500,300]


#전체,첫번째 x축 설정 =plt.subplots()
_,sub1conf=plt.subplots()
p1=sub1conf.plot(xData,yData,color="red")
sub1conf.set_xlabel("엑스")
sub1conf.set_ylabel("와이1")

#첫번째 x축 설정 복사
sub2conf=sub1conf.twinx()
p2=sub2conf.plot(xData,yData2,color="green")
sub2conf.set_ylabel("와이2")

# 범례
sub1conf.legend(p1+p2,["빨","녹"])


plt.show()


