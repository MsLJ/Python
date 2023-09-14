# -*- coding:utf-8 -*-

#pip install --upgrade pip setuptools wheel
#pip install opencv-python
#pip install opencv-python==3.4.0.12
import cv2

#[
#    [p p p]
#    [p p p]
#]=> 2차원

a=cv2.imread("C:/lee/z.png",cv2.IMREAD_GRAYSCALE)
print(a)
#색깔부르면 3차원이돼고
# [
#    [[B G R] [B G R] [B G R]]
#    [[B G R] [B G R] [B G R]]
# ]=>3차원
b=cv2.imread("C:/lee/z.png",cv2.IMREAD_COLOR)
print(b)

#무슨 데이터든 1차원으로 만들면 됌
b=b.flatten()
print(b)

#1차원으로 만들면 됨








