# -*- coding:utf-8 -*-

#pip install --upgrade pip setuptools wheel
#pip install opencv-python
#pip install opencv-python==3.4.0.12
#pip3.6 install opencv-python==3.4.0.12 를 설치했음 경로를 직접가서
import cv2

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

a=cv2.imread("C:/lee/z.png",cv2.IMREAD_GRAYSCALE)
print(a)

#크기 조절
# a=cv2.resize(a,dsize=(100,50))#100x50으로
# a=cv2.resize(a,dsize=(0,0),fx=0.3,fy=0.5)#x를 0.3.배 ,y를 0.5배

#자르기
a=a[100:200, 300:400]

#블러
a=cv2.blur(a,(50,50))

plt.imshow(a,cmap="gray")
plt.show()

#대비 늘리기(밝은거 더 밝게,어두운거 더 어둡게)
#a=cv2.equalizeHist(a)
#경계선(10보다 작으면 무시,50보다 크면 선으로 인식)
a=cv2.Canny(a,10,50)
print(a)
plt.imshow(a,cmap="gray")
plt.show()

