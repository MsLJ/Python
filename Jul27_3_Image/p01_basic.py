# -*- coding:utf-8 -*-

#pip install --upgrade pip setuptools wheel
#pip install opencv-python
#pip install opencv-python==3.4.0.12
import cv2

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

a=cv2.imread("C:/lee/z.png",cv2.IMREAD_GRAYSCALE)
print(a)

#픽셀 하나를 [255 0 0]
b=cv2.imread("C:/lee/z.png",cv2.IMREAD_GRAYSCALE)
print(b)
#BGR->RGB로
b=cv2.cvtColor(b,cv2.COLOR_BGR2RGB)
print(b)

plt.imshow(a)
plt.show()
